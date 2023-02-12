import unittest
from tyre.carrigan_tyre import CarriganTyre 

class TestCarriganTyre(unittest.TestCase):

    def test_carrigan_tyre_should_be_serviced(self):
        tyres_status = [0.1, 0.4, 0.4, 0.9]
        tyre = CarriganTyre(tyres_status)
        self.assertTrue(tyre.needs_service())

    def test_carrigan_tyre_should_not_be_serviced(self):
        tyres_status = [0.1, 0.4, 0.4, 0.3]
        tyre = CarriganTyre(tyres_status)
        self.assertFalse(tyre.needs_service())