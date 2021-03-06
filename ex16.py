from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# wait for ctrl-c or return
raw_input("?")

# open the file and store in variable
print "Opening the file..."
target = open(filename, 'w')

# emptying anything inside of the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# get 3 lines from the user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write the 3 lines to the file, separating each with a newline
target.write(line1+"\n"+line2+"\n"+line3+"\n")

# close the file
print "And finally, we close it."
target.close()
