from datetime import datetime

from pydantic import Field, conlist

from src.infrastructure.api.schemas import CustomBaseModel


class WorkInfoSchema(CustomBaseModel):
    work_status: str = Field(alias="workStatus")
    description: str = Field(alias="description")
    registered_at: datetime = Field(alias="registeredAt")


class ListWorkSchema(CustomBaseModel):
    total: int
    items: conlist(WorkInfoSchema)


class WorkSchema(CustomBaseModel):
    work_status: str = Field(alias="workStatus")
    description: str = Field(alias="description")


class RegistrationSuccess(CustomBaseModel):
    work_id: str = Field(alias="WorkID")
    status: str
    message: str
