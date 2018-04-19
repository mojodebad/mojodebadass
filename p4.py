cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars - drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_passengers_per_car=passengers/cars_driven

print("there are {} cars available".format(cars));
print("there are only ",drivers,"drivers available.")
print("there will be {} cars undriven".format(cars_not_driven))
print("we can transport {} people today \n we have {} to carpool today\n we need to put about {} ".format(carpool_capacity,passengers,average_passengers_per_car))
