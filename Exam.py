# Riley Schippers
# 3,15,2019
# Final Exam Project

'''
This is a small survey that asks for you name, age, favorite sport, favorite color, and last guess a number one through ten.
'''
#Adding a small greeting function for your name and age

name = input('What is your name?:')

age = -1

try:
    age = int(input('How old are you?: '))
except ValueError:
    print('\n''That isn\'t correct' )

print('\n''Name:', name)
print('Age:', age)
