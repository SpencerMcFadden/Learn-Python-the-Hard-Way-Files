# creating the function to print the number of food items
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % (boxes_of_crackers)
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    

# hardcoding in numbers as parameters
print "We can just give the function numbers directly"
cheese_and_crackers(20, 30)


# coding variables and then using those as parameters
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# performing math functions in the parameters
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# performing math functions in the paramters using variables in addition to numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
