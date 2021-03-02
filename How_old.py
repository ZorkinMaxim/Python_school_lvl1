year_of_birth = int(input("What year you were born?" ))
age = 2020 - year_of_birth

if year_of_birth > 2020 or year_of_birth < 1900:
    print("Wrong year!")
elif age >= 1 and age <= 3:
    print(age, "years old, baby")
elif age >= 4 and age <= 9:
    print(age, "years old, kid")
elif age >= 10 and age <= 15:
    print(2020 - age, "years old, teen")
elif age >= 16 and age <= 18:
    print(2020 - age, "years old, young")
elif age >= 19 and age <= 50:
    print(age, "years old, adult")
elif age >= 51 and age <= 999:
    print(age, "years old, old")