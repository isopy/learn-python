cars = 100  # number of cars total
space_in_a_car = 4.0  # number of seats per car
drivers = 30  # total number of drivers available today
passengers = 90  # total number of passengers to transport
cars_not_driven = cars - drivers  # number of empty cars
cars_driven = drivers  # you need 1 driver per car              
carpool_capacity = cars_driven * space_in_a_car # how many seats are available
average_passengers_per_car = passengers / cars_driven # how many passengers (on average) can fit in each car


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
