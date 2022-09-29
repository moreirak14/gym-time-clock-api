import unittest
import uuid
from dataclasses import is_dataclass

from src.commons.domain.exceptions import InvalidUUID
from src.commons.domain.value_objects import UniqueEntityId


class TestUniqueEntityIdUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with self.assertRaises(InvalidUUID) as error:
            UniqueEntityId(id="Fake ID")
        self.assertEqual(error.exception.args[0], "ID must be a valid UUID")

    def test_accept_uuid_passed_in_constructor(self):
        value_object = UniqueEntityId(
            id="6eac08e5-5a54-4d2b-afeb-16253d0e75fb")
        self.assertEqual(value_object.id,
                         "6eac08e5-5a54-4d2b-afeb-16253d0e75fb")

        uuid4_value = uuid.uuid4()
        value_object_uuid4 = UniqueEntityId(id=str(uuid4_value))
        self.assertEqual(value_object_uuid4.id, str(uuid4_value))

    def test_generate_id_when_no_passed_id_in_constructor(self):
        value_object_uuid4 = UniqueEntityId()
        self.assertTrue(uuid.UUID(value_object_uuid4.id))
