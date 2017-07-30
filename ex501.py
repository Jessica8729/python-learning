# -*- coding: utf-8 -*-
name = 'Jessica Liu'
age = 44 # not a lie
height = 165 # cm
weight = 58 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print ("let's talk about %s." % name)
print ("She's %d cm tall." % height)
print ("She's %d kg heavy." % weight)
print ("Actually that's not too heavy.")
print ("She's got %s eyes and %s hair." % (eyes, hair))
print ("Her teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get in exactly right
print ("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))