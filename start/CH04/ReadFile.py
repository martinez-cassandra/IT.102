#Created by Cassandra


'''
Opens a file and write the content of response from certain questions
'''

#List of questions to ask the user
questions = [
    "What is your name? ",
    "What is your favorite color? ",
    "What is your first pets name? ",
    "What is your mother's maiden name?",
    "What elementary school did you attend? "

]

#Create a list to save responses
answers = []

#Loop through each question and save the outcome to answers
for q in questions:
     ans = input(q)
     answers.append(ans)


'''
Write all answers to a file safely
'''
with open("hackme.txt", "w") as file:
    for line in answers:
        file.write(line + "\n")


'''
Creating a script to open a file and read the contents CURRENTLY NOT IN USE
'''

with open("hackme.txt", "r") as example:
    content = example.read()
    print(content)