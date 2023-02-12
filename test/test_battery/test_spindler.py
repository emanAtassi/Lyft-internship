import unittest
from datetime import datetime
from battery.spindler import SpindlerBattery


class TestSpindler(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        spindler = SpindlerBattery(last_service_date, today)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler = SpindlerBattery(last_service_date, today)
        self.assertFalse(spindler.needs_service()) 