from battery.battery import Battery

class SpindlerBattery(Battery):

    YEARS_TO_UPDATE = 2

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date  = current_date
    
    def needs_service(self):
        return self.current_date.year - self.last_service_date.year > self.YEARS_TO_UPDATE
    
    
