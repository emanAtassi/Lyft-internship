import unittest
from datetime import datetime
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class TestSpindler(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler = SpindlerBattery(last_service_date, today)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler = SpindlerBattery(last_service_date, today)
        self.assertFalse(spindler.needs_service())


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
    


class TestCapuletEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):

        current_mileage = 30001
        last_service_mileage = 0
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):

        current_mileage = 29000
        last_service_mileage = 0
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.engine_should_be_serviced())


class TestWilloughbyEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):

        current_mileage = 60001
        last_service_mileage = 0
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):

        current_mileage = 59000
        last_service_mileage = 0
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.engine_should_be_serviced())   

 
class TestSternmanEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):

        warning_light_on = True
        sternman = SternmanEngine(warning_light_on)
        self.assertTrue(sternman.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):

        warning_light_on = False
        sternman = SternmanEngine(warning_light_on)
        self.assertFalse(sternman.engine_should_be_serviced())
  

if __name__ == '__main__':
    unittest.main()