import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):

        warning_light_on = True
        sternman = SternmanEngine(warning_light_on)
        self.assertTrue(sternman.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):

        warning_light_on = False
        sternman = SternmanEngine(warning_light_on)
        self.assertFalse(sternman.engine_should_be_serviced())