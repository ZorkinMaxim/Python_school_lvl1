import string
# CRUD - Create Read Update Delete + operations
############### DATA ##########################
terms = ['Python']

menu = """
MENU
##############
1. Add term
2. Print terms
3. Edit term
4. Delete term
0. Exit
##############
Enter option:
"""
############### Logic ########################
while True:
    option = int(input(menu))
    if option == 1:
        term = input('Enter new term: ')
        term = term.strip()
        term = term.capitalize()
        correct = string.ascii_letters
        for index in range(len(terms)):
            if term[index] not in correct:
            #if not term.isalpha():
                print('Error! Must be only latin letters')
                break
            elif len(term) >= 2:
                if term not in terms:
                    terms.append(term)
                else:
                    print(f'Error! The term "{term}" exists!')
            else:
                print('Error! Must be at least 2 symbols')

    if option == 2:
        print('\nTerms in vocabulary:', len(terms))
        for index in range(len(terms)):
            print(index + 1, f"'{terms[index]}'")

    if option == 3:
        term = input('Enter existing term: ')
        term = term.strip()
        term = term.capitalize()
        if term in terms:
            new_term = input('Enter new term: ')
            new_term = new_term.strip()
            new_term = new_term.capitalize()
            index = terms.index(term)
            terms[index] = new_term
        else:
            print(f'Error! The term "{term}" DOES NOT exists!')

    if option == 4:
        term = input('Enter existing term: ')
        term = term.strip()
        term = term.capitalize()
        if term in terms:
            terms.remove(term)
        else:
            print(f'Error! The term "{term}" DOES NOT exists!')

    if option == 0:
        print('Thank you!')
        break
