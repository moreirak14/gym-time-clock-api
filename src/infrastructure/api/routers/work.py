import logging

from fastapi import APIRouter, HTTPException, status

from src.commons.abstracts.sqlalchemy import SqlAlchemyUnitOfWork
from src.infrastructure.services.work import WorkServiceQuery

work_router = APIRouter(prefix="/work", tags=["Work"])
logger = logging.getLogger(__name__)


@work_router.get("/")
def list_works():
    try:
        service = WorkServiceQuery(uow=SqlAlchemyUnitOfWork())
        return service.list_all_works()
    except Exception as error:
        logger.exception(f"Error: {error}")
        return HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=dict(message="Ocorreu um erro ao buscar dados dos usuários")
        )
