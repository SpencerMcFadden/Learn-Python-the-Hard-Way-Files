i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
        
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
     
print "The numbers: "

for num in numbers:
    print num
    
    
# recreating the while loop in a function
print "\nCoverting while-loop to function. drill_1"
# defining the function
def drill_1(n):
    # setting i to 0 and creating a new list to use
    i = 0
    numbers1 = []
    # the while loop, n is whatever number you put into the function
    while i < n:
        print "Item: %d" % i
        numbers1.append(i)
        i += 1
    print numbers1
    
# calling the function with n being 3
print "\nusing drill_1 with n = 3"
drill_1(3)

# calling the function with n being 8
print "\nusing drill_1 with n = 8"
drill_1(8)

print "\nCreating function drill_3 to allow variable step size"
def drill_3(n, s):
    i = 0
    numbers3 = []
    while i < n:
        print "Item: %d" % i
        numbers3.append(i)
        i += s
    print numbers3
    
print "\nusing drill_3 with n = 12 and s = 3"
drill_3(12, 3)



print "\ndrill_5 uses a for-loop and range instead"
def drill_5(n, s):
    # need to specify starting point of 0 so Python reads the other elements correctly
    numbers5 = range(0, n, s)
    for i in numbers5:
        print "Item: %d" % i
    print numbers5
    
drill_5(14, 4) 
