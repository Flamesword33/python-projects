x = 0
y = 12

print('Enter your favourite number: ', end = '')

user_input = input()

y = int(user_input)

for a in range(y):
    x = x + 1
    for b in range(x):
        print('* ', end = '')
    print('')



##def rock_paper_scissors(computer_input):
##
##
##    print('Choose from rock paper or scissors : ', end = '')
##
##    user_input = input()
##
##    if user_input == computer_input:
##        print('draw')
##    elif user_input == 'p':
##        
##
##def main():
##    rock_paper_scissors('p')
##    rock_paper_scissors('g')
