from datetime import datetime

from src.infrastructure.api.schemas import CustomBaseModel
from pydantic import Field, conlist


class WorkInfoSchema(CustomBaseModel):
    work_status: str = Field(alias="workStatus")
    description: str = Field(alias="description")
    registered_at: datetime = Field(alias="registeredAt")


class ListWorkSchema(CustomBaseModel):
    total: int
    items: conlist(WorkInfoSchema)
