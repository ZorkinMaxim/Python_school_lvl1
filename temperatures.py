week_days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
week_temp = [ 15,   14,   -13,  12,   -11,  10,   9]

for index in range(len(week_days)):
    #print(f'{week_days[index]} {week_temp[index]:3}')
    if week_temp[index] < 0:
        print(f'{week_days[index]} {week_temp[index]:3} [cold]')
    else:
        print(f'{week_days[index]} {week_temp[index]:3}')

s = 0
for index in range(len(week_temp)):
    s += week_temp[index]

avg = s / len(week_temp)
print('\nAvg temp =', avg)