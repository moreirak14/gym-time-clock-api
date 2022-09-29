import uuid
from dataclasses import dataclass, field

from src.commons.domain.exceptions import InvalidUUID


@dataclass(frozen=True)
class UniqueEntityId:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        id_value = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self, "id", id_value)
        self._is_validate()

    def _is_validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as error:
            raise InvalidUUID() from error

    def __str__(self):
        return f"{self.id}"
