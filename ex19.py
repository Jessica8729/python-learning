def cheese_and_crackers (cheese_amount, boxes_of_crackers):
	print ("You have %d cheese!" % cheese_amount)
	print ("You have %d boxes of crackers!" % boxes_of_crackers)
	print ("Man that's enough for a party!")
	print ("Get a blanket. \n")


print ("We can just give the function numbers directly:")
cheese_and_crackers (20, 30)


print ("Oh, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print ("We can even do math inside two:")
cheese_and_crackers (20 + 10, 5 + 6)


print ("And we can combine the two, variables and math:")
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)