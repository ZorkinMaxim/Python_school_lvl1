import csv

def loadStats():
    file_name = "data/pop070100_20201112-110937.csv"
    file = open(file_name, 'r')

    file_reader = csv.reader(file, delimiter=',')

    rows = []
    for row in file_reader:
        rows.append(row)   #bidimensional list/array
    return rows

######################################################

# data = loadStats()
# for row in data[4:8]:
#     if len(row) >= 1:
#         print(f"{row[0]:>20s}", end="|")
#         for cell in row[1:7]:
#             print(f"{cell:>3}", end="|")
#     print('\n','-'*100)

data = loadStats()
def printByCountry(country_name, year=2014):
    start_year = 2014
    period = year - start_year
    for row in data[4:]:
        if len(row) >= 1:
            if row[0] == country_name:
                print(f"{row[0]:>20s}", end="|")
                total = []
                for cell in row[1 + period * 6:7 + period * 6]:
                    if cell == "-":
                        cell = cell.replace("-","0")
                    cell = int(cell)
                    total.append(cell)
                    print(f"{cell:>3}", end="|")
                print(f" Total = {sum(total)} immigrants")

printByCountry("Romania", 2015)




