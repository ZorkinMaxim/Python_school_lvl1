food_1_name       = 'Pizza'
food_2_name       = 'Salad'
drink_1_name      = 'Juice'
food_1_price      = 100
food_2_price      = 150
drink_1_price     = 50
food_1_available  = 5
food_2_available  = 5
drink_1_available = 5

food_1_quantity   =  int(input('How many ' + food_1_name + ' do you want ?'))
food_2_quantity   =  int(input('How many ' + food_2_name + ' do you want ?'))
drink_1_quantity  =  int(input('How many ' + drink_1_name + ' do you want ?'))

if food_1_quantity > food_1_available or food_1_quantity <= 0:
    print("Error! Chenge the amount of food!")
    exit()
if food_2_quantity > food_2_available or food_2_quantity <= 0:
    print("Error! Chenge the amount of food!")
    exit()
if drink_1_quantity > drink_1_available or drink_1_quantity <= 0:
    print("Error! Chenge the amount of food!")
    exit()

order_cost = food_1_quantity * food_1_price + food_2_quantity * food_2_price + drink_1_quantity * drink_1_price

print( ' You have ordered: ',"\n", food_1_quantity, ' x ', food_1_name,"\n",\
                           food_2_quantity, ' x ', food_2_name,"\n",\
                           drink_1_quantity, ' x ', drink_1_name,"\n", 'Total', ' = ', order_cost, "mdl")

delivery = 150

for t in range(11):
    d = input("Do you want delivery? y \ n ")
    if d == "y":
        if order_cost < 1000:
            total_price = order_cost + 150
            print("Delivery cost = 150 mdl")
            print("To pay = ", total_price, "mdl")
            break
        else:
            total_price = order_cost + 0
            print("Free delivery")
            print("To pay = ", total_price, "mdl")
            break
    elif d == "n":
        print("To pay = ", order_cost, "mdl")
        break
    else:
        print("Wrong answer! Try again!")