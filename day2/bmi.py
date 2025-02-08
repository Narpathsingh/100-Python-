#body mass index
#weight / height * height

weight = int(input('Enter your weight in kg? \n'))
height = int(input('Enter your height in cm? \n'))

bmicalculator = weight / (height ** 2)

if bmicalculator < 18.5:
    print('underweight')
elif bmicalculator > 18.5 and bmicalculator < 25:
    print('normal weight')
elif bmicalculator > 25:
    print('overweight')
# print("your'e bmi value is ", bmicalculator)



