def while_loop(top,plus):
    i = 0
    numbers = []

    while i < top:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i+plus

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

top = 10
plus = 2

while_loop(top, plus)