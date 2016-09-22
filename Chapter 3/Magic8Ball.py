# function call with return value with added feature
import random


def getAnswer(answerNumber):
    try;
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


answer = ''
while answer != 'N':
    print('What is your question?')
    question = input()
    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(question + '... ' + fortune)
    print('Do you have another question? (Y or N)')
    answer = str.upper(input())

print('Thank you!')
