import math

class Airplane:
    def __init__(self, initX, initY, cons, init_fuel):
        self.position = (initX, initY)
        self.consumption = cons
        self.fuel_level = init_fuel

    def goto(self, X,Y):
        dist = math.sqrt((X-self.position[0])**2 + (Y-self.position[1])**2)
        if dist*self.consumption > self.fuel_level: return False
        else:
            self.position = (X, Y)
            self.fuel_level -= dist*self.consumption
            return True

    def refuel(self, f):
        self.fuel_level += f
