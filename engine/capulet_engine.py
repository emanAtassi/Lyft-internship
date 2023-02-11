from engine.engine import Engine

class CapuletEngine(Engine):

    MILEAGE_TO_SERVICE = 30000

    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > self.MILEAGE_TO_SERVICE
