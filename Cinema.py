# Dubossary city Cinema!

# LEGEND
# "u" - free place
# "V" - free VIP place
# "x" - occupied place
# "X" - occupied VIP place
# Code for VIP ticket - VIP777

places_map = "uuVVVVuu"

while True:
    print("\n", places_map, sep="")
    print("12345678\n")
    free_places = 0
    occupied_places = 0

    for p in places_map:
        if p == "u" or p == "V":
            free_places += 1
        elif p == "x" or p == "X":
            occupied_places += 1
        else:
            pass
    print("Free places -", free_places)
    print("Occupied places -", occupied_places)

    print("\nMENU")
    print("1. Bye ticket")
    print("2. Cancel ticket")
    print("0. Exit")

    option = input("Which option do you select?")
    if option == "1":
        place = int(input("Which place do you want to choose?")) - 1
        if places_map[place] == "u":
            print("Ok!")
            print("Price - 50 MDL")
            places_map = places_map[:place] + "x" + places_map[place+1:]
        elif places_map[place] == "V":
            code = input("You selected a VIP place, please enter a code:")
            if code == "VIP777":
                print("Thank you for choosing VIP place!")
                print("Price - 150 MDL")
                places_map = places_map[:place] + "X" + places_map[place+1:]
            else:
                print("Error")
        elif places_map[place] == "x" or "X":
            print("Occupied!")
    if option == "2":
        place = int(input("Which place do you want to cancel?")) - 1
        if places_map[place] == "x":
            print("Ok!")
            places_map = places_map[:place] + "u" + places_map[place+1:]
        elif places_map[place] == "X":
            print("Ok!")
            places_map = places_map[:place] + "V" + places_map[place+1:]
        elif places_map[place] == "u" or "V":
            print("The place is free! You can not cancel it!")
    if option == "0":
        print("Thank you!")
        break