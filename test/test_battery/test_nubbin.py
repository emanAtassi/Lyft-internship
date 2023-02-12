import unittest
from datetime import datetime
from battery.nubbin import NubbinBattery


class TestNubbin(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        nubbin = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        nubbin = NubbinBattery(last_service_date, today)
        self.assertFalse(nubbin.needs_service())  