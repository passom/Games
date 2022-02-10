from answers import *
quiz_select = input('Welcome to this Quiz. The theme of this Quiz is can be chosen by the player. Please type either of the following: Football, League of Legends, Music ')

points = 0
if quiz_select.lower() == 'football':
    print(f"Let's play the {quiz_select} quiz.")
    #question 1
    print()
    print()
    print('Question 1')
    print()
    print()
    answer = input('Who was the runner-up in the Fifa World Cup (Men) in 2018?: ').lower()
    if answer.lower() in answers_football:
        print('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print(f'Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points)
    #question 2
    print()
    print()
    print('Question 2')
    print()
    print()
    answer = input('How many goals did Christiano Ronaldo score in the UEFA Euro 2016? ')
    if answer.lower() in answers_football:
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print(f'Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points) 
    #question 3
    print()
    print()
    print('Question 3')
    print()
    print()
    answer = input('In which year did the first UEFA Champions League final take place?: ')
    if answer.lower() in answers_football:
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print(f'Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points) 
    #question 4
    print()
    print()
    print('Question 4')
    print()
    print()
    answer = input('Who was the first player to score a hattrick in the Bundesliga? (firstname lastname) ')
    if answer.lower() in answers_football:
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print(f'Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points)


if quiz_select.lower() == 'league of legends':
    print(f"Let's play the {quiz_select} quiz.")
    #question 1
    print()
    print()
    print('Question 1')
    print()
    print()
    answer = input('Which season of League of Legends started in 2022? (please type a number) ')
    if answer.lower() == '12':
        print('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!') 
        if points > 0:
            points -= 1
        print('Current score:', points)
    #question 2
    print()
    print()
    print('Question 2')
    print()
    print()
    answer = input('Which player is mostly referred the be the GOAT of professional League of Legends? ')
    if answer.lower() in ['faker', 'lee sang-hyeok', '이상혁']:
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points) 
    #question 3
    print()
    print()
    print('Question 3')
    print()
    print()
    answer = input('Which team won Worlds the most amount of times? ')
    if answer.lower() in ['skt t1', 'skt', 'sk telekom t1', 'sk telekom', 't1', 'sk텔레콤 t1', 'sk 텔레콤 t1']:
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points) 
    #question 4
    print()
    print()
    print('Question 4')
    print()
    print()
    answer = input('Which play is xPeke know best for? (one word) ')
    if answer.lower() == 'backdoor' or answer == 'xpeke':
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points)




if quiz_select.lower() == 'music':
    print(f"Let's play the {quiz_select} quiz.")
    #question 1
    print()
    print()
    print('Question 1')
    print()
    print()
    answer = input('How many studio albums did AC/DC publish? (until 2022) ')
    if answer.lower() == '18':
        print('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!') 
        if points > 0:
            points -= 1
        print('Current score:', points)
    #question 2
    print()
    print()
    print('Question 2')
    print()
    print()
    answer = input('Is a violin likely to be in an orchestra? (type Yes or No) ')
    if answer.lower() == 'yes':
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points) 
    #question 3
    print()
    print()
    print('Question 3')
    print()
    print()
    answer = input('Who is considered to be the "King of Pop"? (firstname lastname) ')
    if answer.lower() == 'michael jackson':
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points) 
    #question 4
    print()
    print()
    print('Question 4')
    print()
    print()
    answer = input('Jimi Hendrix, Brian Jones, Kurt Cobain and Amy Winehouse are all part of a sad club. What is the name of this club? ')
    if answer.lower() == '27 club' or answer == 'club 27':
        print ('Correct!')
        points += 1
        print('Current score:', points)
    else:
        print('Incorrect!')
        if points > 0:
            points -= 1
        print('Current score:', points)

else:
    quit()