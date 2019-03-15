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

#Added A question that asks for your favorite sport and number

sport = input('what is your favorite sport?:')

favorite_number = input('What is your favorite number?:')

print('\n''Favorite Sport:', sport)
print('\n''Favorite Number:', favorite_number)

#Adding A question for your favorite color
for i in range(1):
    Color = input('What is your favorite color?:')
    print('\n''Favorite Color:', Color)

#Added a question for guessing a number one through ten
my_number = 1

print ("Guess my number of one through ten")
print ("")

guess = int(input("Enter a guess: "))


while guess != my_number:
    print ("")
    print ("No")
    guess = int(input("Enter a guess: "))

print ("")
print ("Good job you win!")

#Added a small parameter for the you win the guess my number

def print_multiple_times(string, times):
    for i in range(times):
        print(string)
print_multiple_times('You Win!!!!',7)

