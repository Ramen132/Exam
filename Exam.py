# Riley Schippers
# 3,15,2019
# Final Exam Project

'''
This is a small survey that asks for you name, age, favorite sport, favorite color, and last guess a number one through ten.
'''
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