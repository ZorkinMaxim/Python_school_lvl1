#def drowMountain(height):
#    for i in range(height):
#        if i == 0:
#            print('      #')
#        elif i == 1:
#            print('     # #')
#        elif i == 2:
#            print('#####   #####')
#
#drowMountain(3)


#def drowMountain(height):
#    for i in range(height):
#        if i == 0:
#            print('        #')
#        elif i == 1:
#            print('       # #')
#        elif i == 2:
#            print('      #   #')
#        elif i == 3:
#            print('     #     #')
#        elif i == 4:
#            print('#####       #####')
#
#drowMountain(5)


def drowMountain(height):
    for i in range(height):
        print(' '*(height-i-1)+'#'*(2*i+1))

drowMountain(5)