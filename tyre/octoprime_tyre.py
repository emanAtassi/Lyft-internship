class OctoprimeTyre:

    def __init__(self, tyres_status):
        self.tyres_status = tyres_status

    def needs_service(self):
        return any(x >= 0.9 for x in self.tyres_status)


