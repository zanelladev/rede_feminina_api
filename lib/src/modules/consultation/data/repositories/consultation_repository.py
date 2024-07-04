from lib.src.core.factories.mysql.mysql_factory import MySqlFactory
from lib.src.modules.auth.domain.entities.user_entity import UserEntity
from lib.src.modules.auth.domain.entities.user_role import UserRole
from lib.src.modules.consultation.domain.dtos.requests.consultation_complete_request_dto import (
    ConsultationCompleteRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_create_request_dto import (
    ConsultationCreateRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_edit_request_dto import (
    ConsultationEditRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_fetch_all_request_dto import (
    ConsultationFetchAllRequestDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_complete_response_dto import (
    ConsultationCompleteResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_create_response_dto import (
    ConsultationCreateResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_edit_response_dto import (
    ConsultationEditResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_fetch_all_response_dto import (
    ConsultationFetchAllResponseDto,
)
from lib.src.modules.consultation.domain.entities.consultation_fetch_entity import (
    ConsultationFetchEntity,
)
from lib.src.modules.consultation.domain.repositories.i_consultation_repository import (
    IConsultationRepository,
)


class ConsultationRepository(IConsultationRepository):
    def __init__(self, mysql_factory: MySqlFactory):
        self.mysql_factory = mysql_factory

    async def create(
        self, dto: ConsultationCreateRequestDto
    ) -> ConsultationCreateResponseDto:
        self.mysql_factory.connect()
        cursor = self.mysql_factory.get_cursor()

        sql = "INSERT INTO consultation (date, is_completed, id_user, id_type) VALUES (%s, %s, %s, %s)"
        values = (dto.date, 0, dto.id_user, dto.id_type)
        cursor.execute(sql, values)

        self.mysql_factory.commit()

        select_sql = """
        SELECT id 
        FROM consultation 
        WHERE id_user = %s AND date = %s
        ORDER BY id DESC
        LIMIT 1
        """
        select_values = (dto.id_user, dto.date)
        cursor.execute(select_sql, select_values)
        consultation_id = cursor.fetchone()

        self.mysql_factory.close_connection()

        return ConsultationCreateResponseDto(
            id=consultation_id["id"],
            date=dto.date,
            is_completed=0,
        )

    async def edit(
        self, dto: ConsultationEditRequestDto
    ) -> ConsultationEditResponseDto:
        try:

            self.mysql_factory.connect()
            cursor = self.mysql_factory.get_cursor()

            if dto.user.role == UserRole.USER:
                update_sql = """
                UPDATE consultation
                SET date = %s, id_type = %s
                WHERE id = %s AND id_user = %s
                """
                update_values = (dto.date, dto.id_type, dto.id, dto.user.id)
                cursor.execute(update_sql, update_values)

            update_parts = []
            update_values = []

            if dto.date is not None:
                update_parts.append("date = %s")
                update_values.append(dto.date)

            if dto.id_type is not None:
                update_parts.append("id_type = %s")
                update_values.append(dto.id_type)

            update_values.append(dto.id)

            update_sql = f"""
                UPDATE consultation
                SET {', '.join(update_parts)}
                WHERE id = %s
              """

            cursor.execute(update_sql, tuple(update_values))

            self.mysql_factory.commit()

            self.mysql_factory.close_connection()

            return ConsultationEditResponseDto(
                success=True,
            )

        except Exception as e:
            print(f"Error editing consultation: {e}")
            return ConsultationEditResponseDto(
                success=False,
            )

    async def fetchAll(
        self, dto: ConsultationFetchAllRequestDto
    ) -> ConsultationFetchAllResponseDto:
        self.mysql_factory.connect()
        cursor = self.mysql_factory.get_cursor()
        consultations = []

        if dto.user.role == UserRole.USER:
            # Query to fetch all details for the user's consultations within the date range
            own_consultations_sql = """
            SELECT * 
            FROM consultation 
            WHERE id_user = %s AND date BETWEEN %s AND %s
            ORDER BY date DESC
            """
            own_consultations_values = (dto.user.id, dto.start_date, dto.end_date)
            cursor.execute(own_consultations_sql, own_consultations_values)
            for row in cursor.fetchall():
                consultation_entity = ConsultationFetchEntity(
                    date=row["date"],
                    is_completed=row["is_completed"],
                    id=row["id"],
                    id_type=row["id_type"],
                    user=dto.user,
                )
                consultations.append(consultation_entity)

            # Query to fetch id and date for consultations from other users within the date range
            other_users_consultations_sql = """
            SELECT id, date, is_completed, id_type 
            FROM consultation 
            WHERE id_user != %s AND date BETWEEN %s AND %s
            ORDER BY date DESC
            """
            other_users_consultations_values = (
                dto.user.id,
                dto.start_date,
                dto.end_date,
            )
            cursor.execute(
                other_users_consultations_sql, other_users_consultations_values
            )
            for row in cursor.fetchall():
                consultation_entity = ConsultationFetchEntity(
                    date=row["date"],
                    is_completed=row["is_completed"],
                    id=row["id"],
                    id_type=row["id_type"],
                )
                consultations.append(consultation_entity)

        elif dto.user.role == UserRole.ADMIN:
            # For UserRole.ADMIN: Fetch all consultations within the date range
            all_consultations_sql = """
            SELECT * 
            FROM consultation 
            WHERE date BETWEEN %s AND %s
            ORDER BY date DESC
            """
            all_consultations_values = (dto.start_date, dto.end_date)
            cursor.execute(all_consultations_sql, all_consultations_values)
            for row in cursor.fetchall():

                sql = "SELECT * FROM user WHERE id = %s"
                val = (row["id_user"],)
                cursor.execute(sql, val)
                sql_user = cursor.fetchone()

                user_entity = UserEntity(
                    id=sql_user["id"],
                    email=sql_user["email"],
                    cpf=sql_user["cpf"],
                    name=sql_user["name"],
                    surname=sql_user["surname"],
                    social_name=sql_user["social_name"],
                    phone_number=sql_user["phone_number"],
                    role=UserRole(sql_user["role"]),
                )

                consultation_entity = ConsultationFetchEntity(
                    date=row["date"],
                    is_completed=row["is_completed"],
                    id=row["id"],
                    id_type=row["id_type"],
                    user=user_entity,
                )
                consultations.append(consultation_entity)

        self.mysql_factory.commit()
        self.mysql_factory.close_connection()

        # Construct the response DTO with the fetched consultations
        return ConsultationFetchAllResponseDto(
            consultations=consultations,
        )

    async def complete(
        self, dto: ConsultationCompleteRequestDto
    ) -> ConsultationCompleteResponseDto:
        try:
            self.mysql_factory.connect()
            cursor = self.mysql_factory.get_cursor()

            if dto.user.role == UserRole.USER:
                update_sql = """
                UPDATE consultation
                SET is_completed = %s
                WHERE id = %s AND id_user = %s
                """
                update_values = (True, dto.id, dto.id_user)
                cursor.execute(update_sql, update_values)

            if dto.user.role == UserRole.ADMIN:
                update_sql = """
                UPDATE consultation
                SET is_completed = %s
                WHERE id = %s
                """
                update_values = (True, dto.id)
                cursor.execute(update_sql, update_values)

            self.mysql_factory.commit()

            self.mysql_factory.close_connection()

            return ConsultationCompleteResponseDto(
                success=True,
            )

        except Exception as e:
            print(f"Error editing consultation: {e}")
            return ConsultationCompleteResponseDto(
                success=False,
            )
