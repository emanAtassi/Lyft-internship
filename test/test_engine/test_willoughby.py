import unittest
from engine.willoughby_engine import WilloughbyEngine

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