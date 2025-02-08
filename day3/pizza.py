print('Welcome to pizza hut')
size = input('enter the size of the pizza S, M or L ').upper()
pepperoni = input('Do you want to add pepperoni Y or N ').upper()
cheese = input('Do you want to add cheese Y or N ').upper()

bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25
else:
    print('you typed wrong input, please check')

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if cheese == 'Y':
    bill += 1

print(f'your final bill is {bill}')