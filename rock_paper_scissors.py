import random

user_wins = 0
cpu_wins = 0
attacks = ['rock', 'paper', 'scissors', 'q']
wins_needed = input('How many wins do the competitors need to win? Type any number larger than 0: ')

if wins_needed.isdigit():
    wins_needed = int(wins_needed)
else:
    print('Please run the game again and type a number next time.')
    quit()
if wins_needed <= 0:
    print('Please type a number greater than 0.')
    quit()

while True:
    if cpu_wins == wins_needed:
        print(f'The game has ended! The CPU wins! The Score was: CPU {cpu_wins}:{user_wins} YOU.')
        break
    if user_wins == wins_needed:
        print(f'The game has ended! You win! the Score was: YOU {user_wins}:{cpu_wins} CPU. ')
        break
    user_attack = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_attack == 'q':
        print(f'The game has been ended by your choice before a winner was determined! The CPU won {cpu_wins} times. You won {user_wins} times.')
        break
    if user_attack not in attacks:
        print(f'Please type any of the given options: {", ".join(x for x in attacks).title()}')
        continue
    else:
        cpu_pick = random.randint(0, 2)
        cpu_attack = attacks[cpu_pick]
        if user_attack == cpu_attack:
            print(f"It's a draw! The CPU attacked with {cpu_attack.title()}.")
            print(f'Current score: CPU {cpu_wins}:{user_wins} YOU')
        elif user_attack == "rock" and cpu_attack == 'scissors':
            print(f'You win! The CPU attacked with {cpu_attack.title()}.')
            user_wins += 1
            print(f'Current score: CPU {cpu_wins}:{user_wins} YOU')
        elif user_attack == "scissors" and cpu_attack == 'paper':
            print(f'You win! The CPU attacked with {cpu_attack.title()}.')
            user_wins += 1
            print(f'Current score: CPU {cpu_wins}:{user_wins} YOU')
        elif user_attack == 'paper' and cpu_attack == 'rock':
            print(f'You win! The CPU attacked with {cpu_attack.title()}.')
            user_wins += 1
            print(f'Current score: CPU {cpu_wins}:{user_wins} YOU')
        else:
            print(f'The CPU wins! The CPU attacked with {cpu_attack.title()}.')
            cpu_wins += 1
            print(f'Current score: CPU {cpu_wins}:{user_wins} YOU')

print('Goodbye!')
