lift_floor = 5
human_floor = 5

print("  -------")
for f in range(9, -1, -1):
    if f == 0:
        print("P", "| |___|")
    elif f == lift_floor == human_floor:
        print(f, "|L|_H_|")
    elif f == lift_floor:
        print(f, "|L|___|")
    elif f == human_floor:
        print(f, "| |_H_|")
    else:
        print(f, "| |___|")

print("  -------")

if lift_floor < human_floor:
    print("lift ascending")
elif lift_floor > human_floor:
    print("lift descending")
else:
    print("lift arrived")
