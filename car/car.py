from car.serviceable import Serviceable
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.battery import Battery
from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery


    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.needs_service()
