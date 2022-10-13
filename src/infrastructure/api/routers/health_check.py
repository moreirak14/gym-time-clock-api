from fastapi.routing import APIRouter

from src.commons.abstracts.sqlalchemy import SqlAlchemyUnitOfWork
from src.infrastructure.api.schemas.health_check import Message
from src.infrastructure.services.health_check import (
    HealthCheckServiceQuery,
    StatusCheckEnum,
)

health_router = APIRouter()


@health_router.get("/health-check")
def health_check():
    status = {
        "application": StatusCheckEnum.SUCCESS.value,
    }

    check_database = HealthCheckServiceQuery(
        uow=SqlAlchemyUnitOfWork()).status_check_database()
    status |= check_database

    return Message(**status)
