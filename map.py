b_r = int(input("Row?"))
b_c = int(input("Column?"))

for r in range(1, 11):
    for c in range(1, 11):
        if c == 1 or c == 10 or r == 1 or r == 10:
            print("#", end=" ")
        else:
            if r == b_r and c == b_c:
                print("+", end=" ")
            elif r == b_r - 1 and c == b_c or r == b_r + 1 and c == b_c or\
                 r == b_r and c == b_c - 1 or r == b_r and c == b_c + 1:
                print("x", end=" ")
            elif r == b_r - 1 and c == b_c - 1 or r == b_r + 1 and c == b_c + 1 or \
                 r == b_r - 1 and c == b_c - 1 or r == b_r + 1 and c == b_c + 1:
                print("x", end=" ")
            elif r == b_r - 1 and c == b_c + 1 or r == b_r + 1 and c == b_c - 1 or\
                 r == b_r + 1 and c == b_c - 1 or r == b_r - 1 and c == b_c + 1:
                print("x", end=" ")
            else:
                print(".", end=" ")
    print()