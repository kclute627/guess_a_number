# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:43:45 2018

@author: kyclu
"""


def guess_number():

    import random
    # introduction
    number = random.randint(0, 101)
    counter = 1

    print(" You have five guesses to get the number im thinking of correctly... I am thinking of a number between 1 and 100.\n")
    print(' Take a guess: ')
    guess = int(input())

    while counter <= 5:
        if guess == number:
            print('Congrulations you guessed correctly my number was {} and you guessed {}'.format(number, guess))
            break

        else:

            if guess < number:
                print('Your guess was too low you have used {} guess'.format(counter))
                guess = int(input(' Guess agian: '))
                counter = counter + 1

            elif guess > number:
                print('Your guess was too high you have used {} guess'.format(counter))
                guess = int(input(' Guess agian: '))
                counter = counter + 1
    if counter > 5:
        print('You lost the number I was thinking of was {}'.format(number))
