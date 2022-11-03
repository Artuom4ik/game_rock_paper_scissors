import random

count = 0
for i in range(10):
    player = input("Сделайте ход: 1 - камень, 2 - ножницы, 3 - бумага: ")
    player = int(player)
    if player == 1:
        print('Ваш ход - камень')
    elif player == 2:
        print('Ваш ход - ножницы')
    else:
        print('Ваш ход - бумага')
    comp = random.randint(1, 3)
    if comp == 1:
        print('Ход компьютера - камень')
    elif comp == 2:
        print('Ход компьютера - ножницы')
    else:
        print('Ход компьютера - бумага')
    if comp == player:
        print('Ничья!')
    elif comp == 1 and player == 2:
        print('Вы проиграли!')
    elif comp == 2 and player == 3:
        print('Вы проиграли!')
    elif comp == 3 and player == 1:
        print('Вы проиграли!')
    else:
        print('Вы выйграли!')
        count = count + 1
    print('Мои победы', count)
    if count == 3:
        break
