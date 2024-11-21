import unittest
from display import Display
from carpark import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(1, CarPark(), "Test Display", True)

    def test_display_initialized_with_all_attributes(self):
        self.assertEqual(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Test Display")
        self.assertEqual(self.display.is_on, True)

    def test_update(self):
        self.display.update({"message": "Updated message"})

        self.assertEqual(self.display.message, "Updated message")