from abc import ABC
from dataclasses import asdict, dataclass, field

from src.commons.domain.value_objects import UniqueEntityId


@dataclass()
class Entity(ABC):
    unique_entity_id: UniqueEntityId = field(default_factory=UniqueEntityId)

    @property
    def id(self):
        return str(self.unique_entity_id)

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop("unique_entity_id")
        entity_dict["id"] = self.id
        return entity_dict
