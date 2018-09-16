class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.weight=50
    def describe_battery(self):
        print("This car has a ",int(self.battery_size),"-kWh battery.")
        print("This car has a",int(self.weight),'Kg')
my_tesla = ElectricCar('tesla', 'model s', 2016)
tesla=ElectricCar('tesla', 'model F', 2018)
print(tesla.get_descriptive_name())
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()