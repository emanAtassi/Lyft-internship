import unittest
from tyre.octoprime_tyre import OctoprimeTyre 

class TestOctoprimeTyre(unittest.TestCase):

    def test_octoprime_tyre_should_be_serviced(self):
        tyres_status = [0.8, 0.8,0.8, 0.8]
        tyre = OctoprimeTyre(tyres_status)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyres_status = [0.1, 0.4, 0.4, 0.3]
        tyre = OctoprimeTyre(tyres_status)
        self.assertFalse(tyre.needs_service())