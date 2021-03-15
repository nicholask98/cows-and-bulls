# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

import random

def welcome():
    print('Cows and Bulls!')
    print('I have a secret 4 digit number.')
    print('Every digit you guess correctly in the correct place is a “cow”.')
    print('Every digit you guess correctly in the wrong place is a “bull.”')
    print('Try to get the lowest guess count you can!\n')

def error(attempt):
    # FIXME: error()
    return -1
    
def check_attempt(attempt, answer):
    attempt_copy = attempt[:]
    answer_copy = answer[:]
    cows = 0
    bulls = 0
    if attempt != answer:
        for num in range(len(answer[:])):
            if attempt[num] == answer[num]: # Find cows
                attempt_copy.pop(num - cows)
                answer_copy.pop(num - cows)
                cows += 1
        answer = answer_copy
        attempt = attempt_copy
        for num in range(len(answer)): # Find Bulls
            if attempt[num] in answer:
                bulls += 1
        print('Cows: {} Bulls: {}'.format(cows, bulls))
        attempt = input("Guess a four-digit number or enter '0' to quit:\n")
    else:
        print('Answer was:', ''.join(answer))
        print('You win!')
        
        attempt = '0'
    
    return attempt

def main():
    clear()
    generated_number_list = [str(random.randint(0, 9)) for i in range(4)] # creates 4 digit list
    welcome()
    user_attempt = input("Guess a four-digit number: or enter '0' to quit:\n")
    guess_count = 0
    while user_attempt != '0':
        clear()
        guess_count += 1
        print('Guess count:', guess_count)
        user_attempt = check_attempt(list(user_attempt), generated_number_list) # Checks guess and prompts for new guess if wrong

    print('Thanks for playing!')


if __name__ == '__main__':
    main()
