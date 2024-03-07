from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) # Prints text in f

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())  #Prints the line number line_count

current_file = open(input_file) # Open the file input_file

print("First let's print the whole file: \n")

print_all(current_file) # Calls function print_all 

print("Now let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)