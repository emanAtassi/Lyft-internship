from car.car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre



class CarFactory:

    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tyres_status):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyre = CarriganTyre(tyres_status)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage, tyres_status):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyre = OctoprimeTyre(tyres_status)
        car = Car(engine, battery, tyre)
        return car

    @staticmethod
    def create_palindrome(self,current_date, last_service_date, warning_light_on, tyres_status):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tyre = CarriganTyre(tyres_status)
        car = Car(engine, battery, tyre)
        return car     
    
    @staticmethod
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage, tyres_status):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tyre = OctoprimeTyre(tyres_status)
        car = Car(engine, battery, tyre)
        return car    

    @staticmethod
    def create_thovex(self,current_date, last_service_date, current_mileage, last_service_mileage, tyres_status):
        engine = CapuletEngine(current_mileage, last_service_mileage)       
        battery = NubbinBattery(last_service_date, current_date)
        tyre = CarriganTyre(tyres_status)
        car = Car(engine, battery, tyre)
        return car  

     