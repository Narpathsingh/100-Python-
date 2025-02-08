#control flow

print('Welcome to roller coaster')

height = int(input('enter your height in cm? '))
bill = 0

if height >= 120:
    print('you can ride roller coaster')
    age = int(input('enter your age: '))
    if age < 12:
        bill = 5
        print(f'The ticket is ${bill}')
    elif age >= 12 and age <= 18:
        bill = 7
        print(f'The ticket is ${bill}')
    elif age >= 45 and age <= 55:
        bill = 0
        print('you got free ride')
    else:
        bill = 12
        print(f'The ticket is ${bill}')


    wantsphoto = input('Do you want to take photo Y or N ').upper()
    if wantsphoto == 'Y':
        bill += 3
        print(f'your final bill is {bill}')
    else:
        print('Thank you')
else:
    print('you cannot ride roller coaster')





# modulo

# print('Welcome to even and odd')
#
# userinput = int(input('Enter a number you need to check even or odd: '))
# if userinput % 2 == 0:
#     print('The given number is even')
# else:
#     print('The given number is odd')