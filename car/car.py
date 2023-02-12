from car.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tyre):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre


    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.needs_service() or self.tyre.needs_service()
