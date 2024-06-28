from datetime import datetime


class ConsultationCreateRequestDto:
    def __init__(
        self,
        date: datetime,
        id_type: int,
        id_user: int,
    ):
        self.date = date
        self.id_type = id_type
        self.id_user = id_user
