#small_ship = int(input("Where is small ship?"))
big_ship   = int(input("Where is big ship?"))

for x in range(1,11):
    if x == big_ship:
        print("W", end="")
    elif x == big_ship - 1 or x == big_ship + 1:
        print("w", end="")
    else:
        print("~", end="")