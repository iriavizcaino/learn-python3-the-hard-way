print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Text input on the next line
print("How old are you?")
age1 = input()

# More compact
age2 = input("How old are you?")

# Conversion
age3 = int(input("How old are you? (without decimals)"))
age4 = float(input("How old are you? (with decimals)"))
