# 14. Write a python program to generate 100 random lottery tickets and pick two lucky tickets from
# it as a winner and prints the result.
import random


def draw():
    winner1 = random.randint(1000, 1100)
    winner2 = random.randint(1000, 1100)
    if winner1 != winner2:
        print(f'Winner1: {winner1}    Winner2: {winner2}')
    else:
        draw()


draw()
