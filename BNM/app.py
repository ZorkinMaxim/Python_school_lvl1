from bnm import loadData

currencies = loadData()

#for c in currencies:
#    print(c)

#print(currencies['EUR']['name'],'=', currencies['EUR']['k2'])

def changeCurrency():
    change_cur = input('Enter currency for change: ').upper()
    amount = float(input('Enter the amount: '))
    recive_cur = input('Which currency do you want to recive? ').upper()
    after_change = amount * currencies[change_cur]['k2'] / currencies[recive_cur]['k2']
    print('#####################################')
    print(f'{amount} {currencies[change_cur]["acode"]} = {after_change} {currencies[recive_cur]["acode"]}')
    print('#####################################')
    return change_cur, recive_cur, after_change


def menu(title, options):
    print(f'##### {title:^15} #####')
    for k in options:
        print(f'{k}. {options[k]}')
    print(f'##### {"Choose Option":^15} #####')

    selected = int(input('>>'))
    if selected not in options:
        print('Wrong option!')
    return selected


while True:
    result = menu('Main', {
        1: 'View all currencies',
        2: 'Change',
        0: 'Exit'
    })

    if result == 1:
        for c in currencies:
            print(f"{c} {currencies[c]['k2']}")
    elif result == 2:
        changeCurrency()
    elif result == 0:
        break
