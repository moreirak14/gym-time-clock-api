import logging
from dataclasses import dataclass
from typing import List, Optional

from src.commons.abstracts.sqlalchemy import SqlAlchemyUnitOfWork
from src.domain.work.entity.work import Work, WorkStatus
from src.infrastructure.api.schemas.work import (
    ListWorkSchema,
    WorkInfoSchema,
    WorkSchema,
)

_logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class WorkServiceQuery:
    uow: SqlAlchemyUnitOfWork
    logger: Optional = _logger

    @staticmethod
    def _list_all_to_schema(data: List) -> List[WorkInfoSchema]:
        return [
            WorkInfoSchema(
                work_status=work.work_status,
                description=work.description,
                registered_at=work.registered_at
            ) for work in data
        ]

    def list_all_works(self):
        with self.uow:
            self.logger.info("Getting works...")
            (total, data) = self.uow.work.list_all()
            items = self._list_all_to_schema(data=data)
        return ListWorkSchema(total=total, items=items)

    def create_work(self, data: WorkSchema):
        with self.uow:
            self.logger.info("Creating work...")
            work = Work(
                work_status=WorkStatus.Input.value if data.work_status == "Input" else WorkStatus.Output.value,
                description=data.description
            )
            self.uow.work.create_work(work=work)
            self.uow.commit()
            return dict(
                work_id=work.id,
                status="Ok",
                message="Dados registrado com sucesso!"
            )
