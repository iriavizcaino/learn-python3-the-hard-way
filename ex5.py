name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

inch2cm = 2.54
pound2kg = 1/2.2046

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {round(height*inch2cm,2)} cm tall")
print(f"He's {weight} pounds heavy")
print(f"He's {round(weight*pound2kg,2)} kg heavy")
print("Actually that's not too heavy")
print(f"Heś got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} and {weight}, I get {total}")