# Use argv to get a filename
from sys import argv

script, filename = argv

# Open the file
txt = open(filename)

# Print a little message
print(f"Here's your file {filename}")
print(txt.read())   # Print the content of txt

# Another way to do it
print("Type the filename again:")
file_again = input ("> ")   

txt_again = open(file_again)

print(txt_again.read())