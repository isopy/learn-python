from sys import argv

script, input_file = argv

def print_all(file):    # defines a function named print_all(file)
    print file.read()   # defines what the funtion does (print the output of the file.read() command) 

def rewind(file):       # defines a function named rewind(file)
    file.seek(0)        # defines what the function will do, moves the cursor or the 'read head' to the beginning of the file

def print_a_line(line_count, file):     # defines a function named print_a_line(line_count, file)
    print line_count, file.readline(),   # defines waht the funtion will do, print line_count variable and the the output of file.readline()

current_file = open(input_file)     # sets the variable current_file = to the output of the open(input_file) command

print "First let's print the whole file :\n"    #prints the line

print_all(current_file)     # calls the print_all function, which does a file.read of current_file, which is equal to the output of the open(input_file) command

print "Now let's rewind, kind of like a tape."    #prints the line

rewind(current_file)    # on the current_file (which is the opened input_file) it calls the rewind function, which moves the 'read head' back to the start of the file

print "Let's print three lines:"    #prints the line

# current_line = 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

current_line = 1                            # sets current_line = 1
print_a_line(current_line, current_file)    # because current_line was set to one, this prints the first line in current_file which is the input_file

current_line += 1                           # setus current_line = to the previous value of current_value + 1 (which is 2)
print_a_line(current_line, current_file)    # now current line is set to 2, so this prints the second line of the current_file which is the input_file

current_line += 1                           # setus current_line = to the previous value of current_value + 1 (which is 3)
print_a_line(current_line, current_file)    # now the current_line is set to three, so this prints the third line in current_file which is the input_file