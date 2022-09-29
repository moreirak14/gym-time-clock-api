import uuid
from dataclasses import dataclass, field
from src.commons.domain.exceptions import InvalidUUID


@dataclass()
class UniqueEntityId:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        self.id = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        self._is_validate()

    def _is_validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as error:
            raise InvalidUUID() from error

