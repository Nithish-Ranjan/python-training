'''rock-paper-scissors game'''

import random

choices=('rock', 'paper', 'scissors')

cpu=random.choice(choices)
player = input('rock, paper, or scissors? ')
player=player.lower()

if cpu==player:
    print('draw')
elif (cpu=='rock' and player=='scissors') or (cpu=='paper' and player=='rock') or (cpu=='scissors' and player=='paper'):
    print('cpu chose', cpu)
    print('cpu wins')
elif (player=='rock' and cpu=='scissors') or (player=='paper' and cpu=='rock') or (player=='scissors' and cpu=='paper'):
    print('cpu chose', cpu)
    print('player wins')
else:
    print('invalid input')