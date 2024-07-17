# 1- Address

street = '111 Eighth Avenue'
city = 'Newyork'
country = 'USA'

address_1 = street + '\n' + city + '\n' + country

address_2 = f'{street}\n{city}\n{country}'

print( 'Your address using + is \n', address_1)

print( 'Your address using f string is \n', address_2)

# 2- slice a statement

statement = 'Earth revolves around the sun'

string_1 = statement[6:14]
string_2 = statement[-3:]
print (string_1 + '\n' + string_2)

# 3- fruit and veggie

fruit = 5
veggie = 3

string_3 = f'I eat {veggie} veggies and {fruit} fruits daily'

print (string_3)

# 4- replace

s='maine 200 banana khaye'

s = s.replace ('200 banana', '10 samosa')

print (s)