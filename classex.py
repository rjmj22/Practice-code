class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
car_1 = vehicle('125', '25000')
car_2 = vehicle('158', '8500')

print(car_1.max_speed)
print(car_2.max_speed, car_2.mileage)