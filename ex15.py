# this line imports argv from the system
from sys import argv

# this line gives two parameters for argv
#script, filename = argv

# this line creates a variable to store the file that is being opened
#txt = open(filename), close()

# this line prints a string and the name of the file and then the contents of the file
#print "Here's you file %r:" % filename
#print txt.read()

# this set of lines gets the filename from the user again and creates a new variable for it 
print "Type the filename again:"
file_again = raw_input("> ")

# this puts the open file in another variable
txt_again = open(file_again), close()

# this line reads the contents of the file variable
print txt_again.read()
