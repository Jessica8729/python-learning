# -*- coding: utf-8 -*-
my_name = 'Jessica Liu'
my_age = 44 # not a lie
my_height = 165 # cm
my_weight = 58 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print ("let's talk about %s." % my_name)
print ("She's %d cm tall." % my_height)
print ("She's %d kg heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("She's got %s eyes and %s hair." % (my_eyes, my_hair))

# this line is tricky, try to get in exactly right
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))