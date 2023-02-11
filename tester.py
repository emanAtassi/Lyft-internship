import unittest
from datetime import datetime
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class TestSpindler(unittest.TestCase):

    def test_battery_should_be_tested(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler = SpindlerBattery(last_service_date, today)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_tested(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler = SpindlerBattery(last_service_date, today)
        self.assertFalse(spindler.needs_service())


class TestNubbin(unittest.TestCase):

    def test_battery_should_be_tested(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        nubbin = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_tested(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        nubbin = NubbinBattery(last_service_date, today)
        self.assertFalse(nubbin.needs_service())  
    



if __name__ == '__main__':
    unittest.main()