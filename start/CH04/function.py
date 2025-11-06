'''
Creating a function
'''

#def creates a function
def send_message():
    if question == 'y':
     print("Yes it is")
    elif question == 'n':
     print('Thats okay tomorrow will be ')
    elif question == 'idk' :
     print('Thats okay')
    else:
     print("Please enter a valid input of y or n for yes or no")


question = input("Is today a good day? Please answer with y or n: ").lower()
send_message()

