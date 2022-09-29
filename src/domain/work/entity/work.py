import enum
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional


class WorkStatus(enum.Enum):
    Input = "input"
    Output = "output"


@dataclass()
class Work:
    work_status: WorkStatus
    description: Optional[str] = None
    registered_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now(timezone.utc))
