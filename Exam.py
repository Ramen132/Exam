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


