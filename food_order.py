def menu(title, options):
    print(f'##### {title:^15} #####')
    for k in options:
        print(f'{k}. {options[k]}')
    print(f'##### {"Choose Option":^15} #####')

    selected = int(input('>>'))
    if selected not in options:
        print('Wrong option!')
    return selected


result = menu('Main', {
    1: 'Food order',
    0: 'Exit'
})
if result == 1:
    result = menu('Menu', {
        1: 'Pizza',
        2: 'Salad',
        3: 'Juice'
    })
if result == 1:
    pizza = int(input('Enter quantity: '))
    print('You have ordered Pizza x', pizza, 'pcs')
elif result == 2:
    salad = int(input('Enter quantity: '))
    print('You have ordered Salad x', salad, 'pcs')
elif result == 3:
    juice = int(input('Enter quantity: '))
    print('You have ordered Juice x', juice, 'pcs')



#print('########## MENU ##########\n')
#
#food = [
#    {
#        'name': 'Pizza',
#        'price': {
#            'value': 100.00,
#            'unit': 'MDL'
#        }
#    },
#    {
#        'name': 'Salad',
#        'price': {
#            'value': 50.00,
#            'unit': 'MDL'
#        }
#    },
#    {
#        'name': 'Soup',
#        'price': {
#            'value': 30.00,
#            'unit': 'MDL'
#        }
#    },
#    {
#        'name': 'Juice',
#        'price': {
#            'value': 20.00,
#            'unit': 'MDL'
#        }
#    }
#]
#
#food_option1 = input('What do you want to order? ')
#
#found = False
#for i in range(len(food)):
#    if food[i]['name'] == food_option1:
#        print('your order index is ',i)
#        print('you have chosen: ', food[i]['name'])
#        quantity1 = int(input('How many?'))
#        cost1 = food[i]['price']['value'] * quantity1
#        found = True
#
#if not found:
#    print('This kind of food temporary is unavailable!')
#
#input('Do you want to add something in order? (y/n)')
#if 'y':
#    food_option2 = input('What do you want to order? ')
#elif 'n':
#    print("Your order will be ready in maximum 30 min!")
#else:
#    print("I don't understand your answer!")
#
#for k in range(len(food)):
#    if food[k]['name'] == food_option2:
#        print('your order index is ',k)
#        print('you have chosen: ', food[k]['name'])
#        quantity2 = int(input('How many?'))
#        cost2 = food[k]['price']['value'] * quantity2
#        found = True
#
#if not found:
#    print('This kind of food temporary is unavailable!')
#
#total = cost1 + cost2
#print('To pay =', total)





#for index in range(len(food)):
#    print(f"{index + 1:2} {food[index]['name']:10}={food[index]['price']['value']:8.2f} {food[index]['price']['unit']}")
#
#print()
#pizza_quantity = int(input('How many ' + food[0]['name'] + ' do you want ?'))
#salad_quantity = int(input('How many ' + food[1]['name'] + ' do you want ?'))
#soup_quantity = int(input('How many ' + food[2]['name'] + ' do you want ?'))
#juice_quantity = int(input('How many ' + food[3]['name'] + ' do you want ?'))
#
#order_cost = pizza_quantity * food[0]['price']['value'] + salad_quantity * food[1]['price']['value'] + \
#    soup_quantity * food[2]['price']['value'] + juice_quantity * food[3]['price']['value']
#
#print(' You have ordered: '"\n", pizza_quantity, ' x ', food[0]['name'],"\n",\
#                           salad_quantity, ' x ', food[1]['name'],"\n",\
#                           soup_quantity, ' x ', food[2]['name'],"\n",\
#                           juice_quantity, ' x ', food[3]['name'],"\n", 'Total', ' = ', order_cost, "MDL")
#
#delivery = 150
#
#for t in range(11):
#    d = input("Do you want delivery? y \ n ")
#    if d == "y":
#        if order_cost < 1000:
#            total_price = order_cost + 150
#            print("Delivery cost = 150 mdl")
#            print("To pay = ", total_price, "mdl")
#            break
#        else:
#            total_price = order_cost + 0
#            print("Free delivery")
#            print("To pay = ", total_price, "mdl")
#            break
#    elif d == "n":
#        print("To pay = ", order_cost, "mdl")
#        break
#    else:
#        print("Wrong answer! Try again!")