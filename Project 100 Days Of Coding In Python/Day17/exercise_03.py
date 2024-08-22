class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        car_description = f"Is a {self.make}, {self.model}, year {self.year}"
        return car_description

class Battery:
    def __init__(self, battery = 70):
        self.battery = battery

    def describe_battery(self):
        print(f"This car has a {self.battery}-kWh battery.")

    def get_range(self):
        if self.battery == 70:
            range = 240
        elif self.battery == 85:
            range = 270
        message = f"This car can go approximately {str(range)} miles on a full charge"
        return message

    def upgrade_battery(self):
        if self.battery != 85:
            self.battery = 85

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

new_electric_car = ElectricCar("Tesla", "Model 3", 2024)
print(new_electric_car.describe_car())
print("\n")
new_electric_car.battery.describe_battery()
print(new_electric_car.battery.get_range())
print("\n")
new_electric_car.battery.upgrade_battery()
new_electric_car.battery.describe_battery()
print(new_electric_car.battery.get_range())