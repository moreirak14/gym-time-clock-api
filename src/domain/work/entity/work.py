from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from src.commons.domain.entities import Entity


class WorkStatus(Enum):
    Input = "input"
    Output = "output"


@dataclass()
class Work(Entity):
    work_status: Optional[WorkStatus] = None
    description: Optional[str] = None
    registered_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now(timezone.utc))
