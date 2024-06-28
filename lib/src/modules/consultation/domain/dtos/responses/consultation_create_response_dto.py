from datetime import datetime


class ConsultationCreateResponseDto:
    def __init__(
        self,
        id: int,
        date: datetime,
        is_completed: bool,
    ):
        self.id = id
        self.date = date
        self.is_completed = is_completed
