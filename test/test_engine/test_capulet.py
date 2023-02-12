import unittest
from engine.capulet_engine import CapuletEngine

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