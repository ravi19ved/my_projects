'''
Python Practice Notes
Date: 20-12-2022
Author @Vedula Ravi Chandra
'''

#This is the first program with some documentation. 

number = 23
guess = int (input('Enter an integer: '))

if guess == number:
    #This is a comment for coder, New Block starts here.
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!')
    #New block ends here

elif guess < number:
    #Another block of code
    print('No, it is a little lower than that')
    #You can do whatever you want in a block....

else:
    print('No, it is a little lower than that')
    #you must have guessed > number to reach here

