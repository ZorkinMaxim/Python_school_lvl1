# Menu
menu_food_name  = ['Pizza', 'Salad', 'Soup']
menu_food_price = [ 100.00,  45.00,   15.00]
menu_food_q     = [      3,      2,      2]

for index in range(len(menu_food_name)):
    print(f"{index + 1:<2} {menu_food_name[index]:7} x {menu_food_q[index]:^3} = \
{                           menu_food_price[index] * menu_food_q[index]:8} MDL")
print('--------------------------------')
s = 0
for index in range(len(menu_food_name)):
    s += menu_food_price[index] * menu_food_q[index]
print(f'   TOTAL         = {s:8} MDL')