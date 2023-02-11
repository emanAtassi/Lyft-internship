from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):


    @abstractmethod
    def needs_service(self):
        pass




