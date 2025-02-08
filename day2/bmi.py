#body mass index
#weight / height * height

weight = int(input('Enter your weight in kg? \n'))
height = int(input('Enter your height in cm? \n'))

bmicalculator = weight / (height * height)
print("your'e bmi value is ", bmicalculator)
