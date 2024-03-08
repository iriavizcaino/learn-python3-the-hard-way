def while_loop(top):
    i = 0
    numbers = []

    while i < top:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i+1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

top = 10

while_loop(top)