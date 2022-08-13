import random

def game():
    
    print('FAVORITE NUMBER GAME')
    computer_num = random.randrange(1, 51) #51 isn't included
    print("I'm thinking of a number...")

    guess_count = 0
    user_guess = 0  #start user guess at any number that computer
                    #dosen't have

    while user_guess != computer_num:
        try:
            user_guess = int(input('Please enter your guess between 1 and 50: '))
            if user_guess < 1 or user_guess > 50:
                    raise Exception()
                             
            elif user_guess < computer_num:
                print('Too low')

                
            elif user_guess > computer_num:
                print('Too high')
                             
            guess_count += 1
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        
        except ValueError:
            print('Invalid Input. Try Again.')
            user_guess = 0

        except:
            print('Invalid Input. Number must be between 1 and 50.')
            user_guess = 0                      

    print('You got it! My favourite number was', computer_num)
    print('It took you ', guess_count , ' tries.')

def games():
    'Continue?'
    again = True
    while again == True:
        game()
        do_again = input('Play Again? : ')
        if do_again.lower()[0] != 'y':
            again = False
    print('Thanks for playing!')

game()
