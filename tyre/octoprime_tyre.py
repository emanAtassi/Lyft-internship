from tyre.tyre import Tyre

class OctoprimeTyre(Tyre):

    def __init__(self, tyres_status):
        self.tyres_status = tyres_status

    def needs_service(self):
        return sum(self.tyres_status) >= 3

