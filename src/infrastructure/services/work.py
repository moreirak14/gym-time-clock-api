import logging
from dataclasses import dataclass
from typing import List, Optional

from src.commons.abstracts.sqlalchemy import SqlAlchemyUnitOfWork
from src.infrastructure.api.schemas.work import ListWorkSchema, WorkInfoSchema

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
