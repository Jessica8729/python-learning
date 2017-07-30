# there's 100 cars.
cars = 100
# there's 4 seats in each car.
space_in_a_car = 4.0
# there's 30 drivers
drivers = 30
# there's 90 passengers.
passengers = 90
# to calculate no. of cars will not be driven
cars_not_driven = cars - drivers
# no. of cars will be driven equal to no. of drivers
cars_driven = drivers
# carpool capacity is decided by cars be driven and space in a car
carpool_capacity = cars_driven * space_in_a_car
# to calculate no. of passengers each car take
average_passengers_per_car = passengers / cars_driven


print ("There are"), cars, "cars available."
print ("There are only"), drivers, "drivers available."
print ("There will be"), cars_not_driven, "empty cars today."
print ( "We can transport"), carpool_capacity, "people today."
print ("We have"), passengers, "to carpool today."
print ("We need to put about"), average_passengers_per_car, "in each car."