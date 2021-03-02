def loadData():
    file = open('data\Official_exchange.csv', 'r')
    #content = file.read()
    #content = file.read().split('\n')
    content = file.readlines()
    content_selected = content[3:-4]

    currencies_dict = {}
    #print(content_selected)
    for line in content_selected:
        data = line[:-1].split(';')
        d = {
            'name': data[0],
            'ncode': int(data[1]),
            'acode': data[2],
            'k1': int(data[3]),
            'k2': float(data[4].replace(',','.'))
        }
        currencies_dict[data[2]] = d

    # print(str(currencies_dict).replace(',','\n'))
    return(currencies_dict)