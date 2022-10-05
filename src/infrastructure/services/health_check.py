import logging
from enum import Enum
from typing import Dict, Optional
from dataclasses import dataclass

from src.infrastructure.services.uow import SqlAlchemyUnitOfWork

_logger = logging.getLogger(__name__)


class StatusCheckEnum(Enum):
    SUCCESS = "Up"
    FAILURE = "Down"


@dataclass()
class HealthCheckServiceQuery:
    uow: SqlAlchemyUnitOfWork
    logger: Optional = _logger

    def status_check_database(self) -> Dict:
        with self.uow:
            try:
                self.uow.session.execute("SELECT 1")
                self.logger.info(
                    f"Service database is {StatusCheckEnum.SUCCESS.value}")
            except Exception as error:
                self.logger.exception(error)
                return {"database": StatusCheckEnum.FAILURE.value}
        return {"database": StatusCheckEnum.SUCCESS.value}
