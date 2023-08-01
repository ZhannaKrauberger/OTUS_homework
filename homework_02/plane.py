"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, n):
        if self.cargo + n > self.max_cargo:
            raise CargoOverload()
        else:
            self.cargo += n

    def remove_all_cargo(self):
        cargo2 = self.cargo
        self.cargo = 0
        return cargo2