import unittest
from datetime import datetime
from dataclasses import is_dataclass
from src.domain.work.entity.work import Work, WorkStatus


class TestWorkUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Work))

    def test_constructor(self):
        work = Work(work_status=WorkStatus.Input)
        self.assertEqual(work.work_status.Input.value, "input")
        self.assertEqual(work.description, None)
        self.assertIsInstance(work.registered_at, datetime)

        registered_at = datetime.now()
        work = Work(
            work_status=WorkStatus.Output,
            description="some description",
            registered_at=registered_at)
        self.assertEqual(work.work_status.Output.value, "output")
        self.assertEqual(work.description, "some description")
        self.assertEqual(work.registered_at, registered_at)

    def test_if_registered_at_is_generated_in_constructor(self):
        work_input = Work(work_status=WorkStatus.Input)
        work_output = Work(work_status=WorkStatus.Output)
        self.assertNotEqual(
            work_input.registered_at,
            work_output.registered_at)