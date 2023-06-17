import logging
from typing import Type, TypeVar

from sqlalchemy.orm import Session

from src.adapters.repositories import SqlAlchemyRepository
from src.domain.work.entity.work import Work

T = TypeVar("T")
_logger = logging.getLogger(__name__)


class WorkRepository(SqlAlchemyRepository):
    def __init__(self, session: Session, obj_type: Type[T], logger=_logger):
        super(WorkRepository, self).__init__(session=session, obj_type=obj_type)
        self.logger = logger

    def list_all(self) -> tuple:
        query = self.session.query(Work)
        query = query.order_by(Work.registered_at)
        total = query.count()
        return total, query.all()

    def create_work(self, work: Work) -> Work:
        self.logger.info("[Create Work] - Initializing service for insert in database")
        self.session.add(work)
        self.logger.info("[Create Work] - Work inserted successfully in database")
        return work
