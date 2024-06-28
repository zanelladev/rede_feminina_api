from lib.src.modules.auth.domain.entities.user_entity import UserEntity


class UserEntityAdapter:
    @staticmethod
    def to_dict(user_entity: UserEntity) -> dict:
        return {
            "id": user_entity.id,
            "email": user_entity.email,
            "name": user_entity.name,
            "surname": user_entity.surname,
            "cpf": user_entity.cpf,
            "phone_number": user_entity.phone_number,
            "role": user_entity.role.value,
            "social_name": user_entity.social_name,
        }
