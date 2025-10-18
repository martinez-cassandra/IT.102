#!/usr/bin/env python3
# example workign with Loops
#By Cassandra

#First we have to gather if the day is good or bad, which requires user input
question = input("Is today a good day? Please answer with y or n: ").lower()

#Analyze the value and print of yes it is
if question == 'y':
    #Create a loop of 10 times saying yea it is"
    number = 1
    while number < 11:
        print("Yes it is")
        number += 1
elif question == 'n':
        print('Thats okay tomorrow will be ')
elif question == 'idk' :
    print('Thats okay')
else:
    print("Please enter a valid input of y or n for yes or no")