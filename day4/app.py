#rock paper scissor
import random



# rock wins scissor loose paper
# paper wins rock loose scissor
# scissor lose rock wins paper

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

symbol = [rock, paper, scissor]
print('Welcome to Rock Paper Scissor')
userinput = int(input('What you want to choose 0 f1or Rock, 1 for Paper, 2 for Scissor '))
if userinput >= 0 and userinput <=2 :
    print(symbol[userinput])

computerchoice = random.randint(0,2)
print(symbol[computerchoice])

if userinput >= 3 or userinput < 0:
    print('please type valid number')
elif userinput == 0 and computerchoice == 2:
    print('you win')
elif userinput == 0 and computerchoice == 2:
    print('you loose')
elif computerchoice > userinput:
    print('computer wins')
elif userinput > computerchoice:
    print('you wins')
elif computerchoice == userinput:
    print('It draw')


