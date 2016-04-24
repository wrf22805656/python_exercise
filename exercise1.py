print ("hello world")
print ("hello again")
print ("I like typing this.")
print ("this is fun.")
print ("Yay! Printing.")
print ("I'd much rather you 'not'. ")
print ("I \"said\" do not touch this")


# A commen, this is so you can read your program later/
# Anathing after the # is ignored by python.

print ("I could have code like this。 ")  # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece
# print "This wont run"
print ("This will run.")


#exercise 2

print ("\n exercise 2\n")
print ("I will now count my chickens:")
print ("hens", 25+30/6)
print ("Roosters", 100 - 25 *3 %4)
print ("Now I will count the eggs:")
print (3+2+1-5+4%2-1/4+6)
print ("Is it true that 3+2 < 5-7?")
print (3+2 < 5-7)
print ("what is 3+2", 3+2)


# exercise 4
print ("\n exercise 4 \n")
cars=100
space_in_a_card =4.0
drivers=3
passengers=90
cars_not_driven=cars -drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_card
average_passengers_per_car=passengers / cars_driven

print ("There are", cars, "cars available")
print ("There are only ", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("we can transport", carpool_capacity, "people today.")
print ("we have", passengers, "to carpool today")
print ("we need to put about", average_passengers_per_car,"in each car")

# exercise 5 #
# this time we'll use something called a "format string."
# every time you put ""- double quotes around a piece of text, you have been making a string


my_name = 'Zed A.Shaw'
my_age = 35 # not a lie
my_height =74 # inches
my_weight =180 # lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'Brown'

print ('\n exercise 5 \n')
print ('let\'s talk about %s.' % my_name)
print ('He\'s %d inches tall.' % my_height)
print ('He\'s %d pounds heavy.' % my_weight)
print ('Actually that\'s not too heavy.')
print ('He\'s got %s eyes and %s hair.' %(my_eyes, my_hair))
print ('His teeth are usually %s depending on the coffee.' % my_teeth)
