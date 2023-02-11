from battery.battery import Battery
from datetime import datetime

class NubbinBattery(Battery):

    YEARS_TO_UPDATE = 4

    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date  = current_date
    
    def needs_service(self):
        date_to_service = self.last_service_date.replace(year= self.last_service_date.year + self.YEARS_TO_UPDATE)
        return self.current_date > date_to_service
    