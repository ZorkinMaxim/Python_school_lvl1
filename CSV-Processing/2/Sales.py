import csv

with open("7.1 SalesJan2009.csv", "r") as f:
    reader = csv.DictReader(f)

    res = {}

    for line in reader:
        city = line['City'].strip()
        price = int(line['Price'])
        try:
            res[city] += price
        except KeyError:
            res[city] = price

    res = sorted(res.items(), key=lambda item: item[1], reverse=True)

    # for element in res:
    #     print(element)

    for a, b in res:
        print(f"{a:35} - {b}")
