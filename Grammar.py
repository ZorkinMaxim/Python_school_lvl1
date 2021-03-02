text = "Hello, I am learning python 3.5. This is cool!"

print()
for index in range(len(text)):
    print(f"{index:3}", end="")
print()
for index in range(len(text)):
    print(f"{text[index]:>3}", end="")
print()

# 3. sentances + format strings
sentances = 0
for index in range(len(text)):
    if text[index].isupper():
        if text[index - 2] in "!.?" and text[index - 1] in " ":
            sentances += 1
            print("  ^", end="")
    elif index == len(text) - 1:
        sentances += 1
        print("  |", end="")
    else:
        print("   ", end="")

print()
# 2. words

words = 0
for index in range(len(text)):
    if text[index] in " ":
        words += 1
        print("  #", end="")
    else:
        print("   ", end="")

print()
# 1. non-space chareacters

non_space_chars = 0
for index in range(len(text)):
    if text[index] not in " ":
        non_space_chars += 1
        print("  -", end="")
    else:
        print("   ", end="")


print()
print(f"Sentances:      {sentances:3}")
print(f"Words:          {words:3}")
print(f"Non space chars:{non_space_chars:3}")
