#Legend
#'_' - land
#'o' - potato
#'Y' - corn
#'0' - tomato

garden = "_ooo_YY_00"

potato_count    = 0
corn_count      = 0
tomato_count    = 0
free_land_count = 0
potato_cost = 50
corn_cost   = 30
tomato_cost = 60

print("\n=== Our Garden ===")

for c in garden:
    print(c, end=" ")

    if c == "o":
        potato_count += 1
    elif c == "Y":
        corn_count += 1
    elif c == "0":
        tomato_count += 1
    elif c == "_":
        free_land_count += 1

garnen_size = potato_count + corn_count + tomato_count + free_land_count
total_cost = potato_count * potato_cost + corn_count * corn_cost + tomato_count * tomato_cost

print("\n\nPotatos -", potato_count, ",", int(potato_count * 100 / garnen_size), "% of all land")
print("Corns -", corn_count, ",", int(corn_count * 100 / garnen_size), "% of all land")
print("Tomatos -", tomato_count, ",", int(tomato_count * 100 / garnen_size), "% of all land")
print("\nTotal cost =", total_cost, "MDL")
