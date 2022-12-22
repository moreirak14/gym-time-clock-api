from __future__ import annotations

from src.adapters.databases import Session
from src.adapters.repositories.work import WorkRepository
from src.commons.abstracts.unity_of_work import AbstractUnitOfWork
from src.domain.work.entity.work import Work

DEFAULT_SESSION_FACTORY = Session


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    default_session_factory = DEFAULT_SESSION_FACTORY

    work: WorkRepository[Work]

    def __init__(self, session_factory=None):
        self.session_factory = (
            session_factory
            if session_factory is not None
            else self.default_session_factory
        )

    def __enter__(self):
        self.session = self.session_factory()
        self.work = WorkRepository(self.session, Work)

    def __exit__(self, *args):
        self.rollback()
        self.session.close()

    def _commit(self):
        self.session.commit()

    def _flush(self):
        self.session.flush()

    def rollback(self):
        self.session.rollback()
