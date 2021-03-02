word = input("Enter a word: ")
print(word)
if word.isalpha():
    print("True")
else:
    print("False")

for c in reversed(word):
    print(c, end='')

print()

word = word[::-1]
print(word)