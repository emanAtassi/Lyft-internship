import unittest
from tyre.tyre import Tyre 

class TestTyre(unittest.TestCase):

    def test_carrigan_tyre_should_be_serviced(self):
        tyres_status = [0.1, 0.4, 0.4, 0.9]
        tyre = Tyre(tyres_status)
        self.assertTrue(tyre.needs_service())

    def test_octoprime_tyre_should_be_serviced(self):
        tyres_status = [0.8, 0.8,0.8, 0.8]
        tyre = Tyre(tyres_status)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyres_status = [0.1, 0.4, 0.4, 0.3]
        tyre = Tyre(tyres_status)
        self.assertFalse(tyre.needs_service())