#tip calculator

print('Welcome to tip calculator')
bill = float(input('Enter the total bill amount: '))
tip = int(input('How much tip would you like to give? 10, 12 or 15 '))
person = int(input('How much person you need to split: '))

tipcal = tip / 100
tipbill = bill * tipcal
billcount = tipbill + bill
billperperson = billcount / person
roundbill = round(billperperson,2)

print('Each person need to : ', roundbill)