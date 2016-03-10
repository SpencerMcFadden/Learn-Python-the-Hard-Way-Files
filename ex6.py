# line 1 makes a string using a formatter
# line 2 creates a string
# line 3 creates a string
# line 4 makes a string using multiple formatters
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

# These two lines print the x and y variables, which are strings
print x
print y

# These lines print strings, but add the x and y strings to them
print "I said: %r." % x
print "I also said: '%s'." % y

# These lines initialize two additional variables, a boolean and a string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# This line prints the joke evaluation string and uses a formatter to add the boolean on the end of it
print joke_evaluation % hilarious

# These lines initialize two strings
w = "This is the left side of..."
e = "a string with a right side."

#This line prints the w and the e strings put together
print w + e
