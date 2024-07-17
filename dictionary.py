# 1- population

population = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}

action = input ('Enter a command:(print,add,remove,query)')

if action == 'print':
    for key in population:
        print(key,'==>',population[key])
elif action == 'add':
    country = input('Enter country to add:')
    if country in population:
        print('Country already exist')
    else:
        count = int(input('Enter population count:'))
        population[country] = count
    print(population)
elif action == 'remove':
    country = input('Enter country to remove:')
    if country in population:
        del population[country]
        for key in population:
            print(key,'==>',population[key])
    else:
        print("Country doesn't exist")
elif action == 'query':
    country = input('Enter country to query:')
    if country in population:
        print(population[country])
    else:
        print("Country doesn't exist")
else:
     print("Wrong command")

# 2- stocks

stocks = {'info': [600,630,620], 'ril': [1430,1490,1567], 'mtl':[234,180,160]}

operation = input ('Enter an operation :(print,add)')

if operation == 'print':
    for stock in stocks:
        average = sum(stocks[stock])/len(stocks[stock])
        print(stock,'==>',stocks[stock],'==>','avg:' ,round(average,2))
elif operation == 'add':
    stock = input('Please enter stock ticker:')
    price = int(input('Enter ticker price:'))
    if stock in stocks:
        stocks[stock].append(price)
    else:
        stocks[stock] = [price]
    print(stocks)

# 3-  circle calculations

from math import pi

def  circle_calc(radius):
    area =round( (pi * (radius ** 2)), 2)
    circumference = round ((2 * pi * radius),2)
    diameter = round((2 * radius),2)
    return area,circumference,diameter

radius =  int(input('Enter Circle radius:'))
area,circumference,diameter = circle_calc(radius)
print('For radius:' , radius, 'The area is:', area, ',the circumference is:', circumference, 'and the diameter is', diameter)
