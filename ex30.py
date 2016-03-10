people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
# else if statement
elif cars < people:
    print "We should not take the cars."
# if no previous statements in this block occur, do this one
else:
    print "We can't decide."
    
if trucks > cars:
    print "That's too many trucks."
# else if statement
elif trucks < cars:
    print "Maybe we could take the trucks."
# if no previous statements in this block occur, do this one
else:
    print "We still can't decide."
    
if people > trucks:
    print "Alright, let's just take the trucks."
# if no previous statements in this block occur, do this one
else:
    print "Fine, let's stay home then."
