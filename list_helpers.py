int_list = [-10, 100, 0, -20, 20]
str_list = ['John', 'Marry', 'Basil']
dict_list = [{'name': 'Pizza', 'price': 100}, {'name': 'Juice', 'price': 50}]

########################################
def printList(l):
    print(f'####### LIST: ({len(l)} elements) #######')
    print(f'[index]   {"value":>20}')
    for i in range(len(l)):
        if type(l[i]) == int or type(l[i]) == str:
            print(f'[{i:5}]   {l[i]:>20} (type: {type(l[i])}')
        if type(l[i]) == dict:
            for k in l[i]:
                value = l[i][k]
                print(f'[{i:5}]   {k:4}:{value:>15} (type: {type(l[i])}')

    print()

########################################
def dictCmp(d):
    for k in d:
        return d[k]
    #return d['name']
    #return d['price']

def sortList(l):
    if type(l[0]) == int or type(l[0]) == str:
        l.sort()
    if type(l[0]) == dict:
        l.sort(key=dictCmp)

########################################
sortList(int_list)
printList(int_list)
sortList(str_list)
printList(str_list)
sortList(dict_list)
printList(dict_list)