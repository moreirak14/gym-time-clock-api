import logging

from fastapi import APIRouter, HTTPException, status

from src.commons.abstracts.sqlalchemy import SqlAlchemyUnitOfWork
from src.infrastructure.api.schemas.work import RegistrationSuccess, WorkSchema
from src.infrastructure.services.work import WorkServiceQuery

work_router = APIRouter(prefix="/work", tags=["Work"])
logger = logging.getLogger(__name__)


@work_router.get("/", status_code=status.HTTP_200_OK)
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


@work_router.post("/")
def create_work(work_data: WorkSchema):
    try:
        logger.debug(f"Data create work: {work_data}")
        service = WorkServiceQuery(uow=SqlAlchemyUnitOfWork())
        work = service.create_work(data=work_data)
        return RegistrationSuccess(**work)
    except Exception as error:
        logger.exception(f"Error: {error}")
        return HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=dict(message="Ocorreu um erro ao criar dados do funcionario.")
        )
