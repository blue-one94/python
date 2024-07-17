# 1- city search

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input('Enter a city : ')

if city in india:
    print('Your city is in India.')
elif city in pakistan:
    print('Your city is in Pakistan.')
elif city in bangladesh:
    print('Your city is in Bangladesh.')
else:
    print("I don't know where your city is.")

#######################################################


city_1 = input('Enter your first city : ')
city_2 = input('Enter your second city : ')

if (city_1 in india and city_2 in india): 
    print("Both cities are in India")
elif (city_1 in pakistan and city_2 in pakistan):
    print("Both cities are in Pakistan")
elif (city_1 in bangladesh and city_2 in bangladesh):
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")


# 2- suger level

suger_level = int(input('Please, Enter you fasting suger level: '))

if suger_level <= 80:
    print("Suger level is low")
elif suger_level > 80 and suger_level < 100:
    print("Suger level is normal")
else:
    print("Suger level is high")
