import enum


class TaskStatus(str, enum.Enum):
    TO_DO = "To do"
    IN_PROGRESS = "In progress"
    COMPLETED = "Completed"
