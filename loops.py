# 1- Heads Count

results = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

heads_count = 0

for result in results:
    if result == "heads":
        heads_count = heads_count + 1

print(heads_count)

# 2-  square of odd numbers between 1 & 10

for num in range(1,10):
    if num%2 == 1:
        print(num**2)
    else:
        continue



# 3- expense test

expense_list = [2340, 2500, 2100, 3100, 2980]

monthes = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

entered_expense = int(input('Enter your expence: '))

for i in range(len(expense_list)):
    if expense_list[i] == entered_expense:
        print ("The expense you entered is for month :", monthes[i] )
        break
    else:
        print ('Expense not found')
        break


# 4- 5 K race

for k in range(5):
    ans = input("Are you tired:(yes/no)" )
    if ans == 'yes':
        print("you didn't finish the race")
        break
    elif k == 4:
        print('Congratulation you finished the race')
    else:
        continue



# 5- print shape

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)