figure = input("what figure to draw?")
#row  = "|" + "\n" + "|"
#line = "-----"

if figure == "line":
    print("-----")
elif figure == "square":
    print("-----", "\n" "|   |" * 2, "\n" "-----", end="")
elif figure == "parallel horizontal lines":
    print("-----\n" * 2, end="")
elif figure == "parallel vertical lines":
    print("|   |\n" * 2, end="")
else:
    print("CAN'T DRAW SUCH FIGURE!")