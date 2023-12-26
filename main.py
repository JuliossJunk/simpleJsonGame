import json
import random


def open_save():
    # Пожалуйста, измените имя файла, если у вас оно иное
    f = open('game.json', encoding='UTF8')

    saved_game = json.load(f)

    print("Загруженно сохранение с такими данными:")
    for k, v in saved_game.items():  # Раскрыть словарь
        print(k, v)
    print("\n\n\n")
    return saved_game


def character_stats(game):
    for k, v in game['character'].items():
        print(k, v)
    print('\n')
    menu(game)


def stats_changer_new(game, item):
    if item == []:
        menu(game)
    game['character']['items'].append(item)
    print('Приобретен предмет - ', item)
    for i in range(len(game['items'])):
        if item == game['items'][i]['name']:
            game['character']['hp'] += game['items'][i]['hp']
            game['character']['damage'] += game['items'][i]['damage']
            break
    menu(game)


def stats_changer_lost(game, item):
    for i in range(len(game['character']['items'])):
        if item == game['character']['items'][i]:
            game['character']['items'].pop(i)
            print('Потерян предмет - ', item)
            break
    for i in range(len(game['items'])):
        if item == game['items'][i]['name']:
            game['character']['hp'] -= game['items'][i]['hp']
            game['character']['damage'] -= game['items'][i]['damage']
            break
    menu(game)


def money_changer_trade(game, lost, get, money):
    game[lost]['money'] -= money
    game[get]['money'] += money
    menu(game)


def shopping(game):
    print(f"Герой {game['character']['name']}, тебе удалось встретить торговца {game['seller']['name']}")
    print(f"{game['seller']['name']} ставит следующую цену предметам:")
    for i in game['items']:
        print(i['name'], '-', i['cost'])
    print('\n')
    choice = input("Что бы ты хотел \n1. Покупать\n2. Продавать\n3. Уйти")
    if choice == '1':
        print(f"У тебя {game['character']['money']} монет, а у торговца есть:")
        if len(game['seller']['items']) != 0:
            for i in range(len(game['seller']['items'])):
                print(f"{i + 1}. {game['seller']['items'][i]}")
            buy = input('Что бы ты хотел купить?(Введите название предмета)')
            if buy in game['seller']['items']:
                for i in range(len(game['items'])):
                    if game['items'][i]['name'] == buy:
                        cost = game['items'][i]['cost']
                        print(buy, 'стоит', cost)
                choice = input('Купить?\n1. Да\n2. Нет')
                if choice == '1':
                    if game['character']['money'] >= cost:
                        stats_changer_new(game, buy)
                        game['seller']['items'] = game['seller']['items'].pop(game['seller']['items'].index(buy))
                        money_changer_trade(game, 'character', 'seller', cost)
                    else:
                        print('Нужно больше золота...')
                        shopping(game)
                else:
                    shopping(game)
            else:
                print('У торговца нет таких вещей на продажу...')
                shopping(game)
        else:
            print('У торговца нет вещей на продажу...')
            shopping(game)
    elif choice == '2':
        print(f"У тебя {game['character']['items']}, а у торговца {game['seller']['money']} золота")
        if len(game['character']['items']) != 0:
            for i in range(len(game['character']['items'])):
                print(f"{i + 1}. {game['character']['items'][i]}")
            buy = input('Что бы ты хотел продать?(Введите название предмета)')
            if buy in game['character']['items']:
                for i in range(len(game['items'])):
                    if game['items'][i]['name'] == buy:
                        cost = game['items'][i]['cost']
                        print(buy, 'стоит', cost)
                choice = input('Продать?\n1. Да\n2. Нет')
                if choice == '1':
                    if game['seller']['money'] >= cost:
                        stats_changer_lost(game, buy)
                        game['seller']['items'].append(buy)
                        money_changer_trade(game, 'seller', 'character', cost)
                    else:
                        print('Торговцу не хватает золота...')
                        shopping(game)
                else:
                    shopping(game)
            else:
                print('У тебя нет таких вещей на продажу...')
                shopping(game)
        else:
            print('У тебя нет вещей на продажу...')
            shopping(game)
    elif choice == '3':
        menu(game)
    else:
        print('Введите правильное действие числом')
        shopping(game)


def hunting(game):
    print('\nГерой вы встретили врагов, готовьтесь к бою')
    if game['character']['hp'] < 1:
        print('Ваше здоровье', game['character']['hp'])
        print('Вы погибли... Герой еще называется...')
        exit_game(game)
    print('Ваше здоровье', game['character']['hp'])
    if len(game['enemy']) != 0:
        print('Здоровье врагов:')
        for i in game['enemy']:
            print(i['name'], i['hp'])
            if i['hp'] < 1:
                print(i['name'], 'побежден!')
                game['character']['money'] += i["money"]
                item=i['items']
                game['enemy'].remove(i)
                stats_changer_new(game, item)
    else:
        print('Вы победили всех монстров герой!\n')
        menu(game)
    choice = input('Выберите действие: \n1. Сражаться \n2. Бежать')
    if choice == '1':
        roll = random.randint(1, 6)
        enemy = game['enemy'].index(random.choice(game['enemy']))
        if 2 < roll < 6:
            print(f"\nОбычная атака по {game['enemy'][enemy]['name']}у")
            game['enemy'][enemy]['hp'] -= game['character']['damage']
        elif roll == 6:
            print(f"\nКритическая атака по {game['enemy'][enemy]['name']}у")
            game['enemy'][enemy]['hp'] -= 2.5 * game['character']['damage']
        else:
            print(f"\nАтакуют вас!")
            game['character']['hp'] -= game['enemy'][enemy]['damage']
        hunting(game)
    elif choice == '2':
        if random.randint(1, 6) > 4:
            print('\nПобег успешен')
            menu(game)
        else:
            print('\nПобег не удался')
            hunting(game)
    else:
        print('Введите корректное действие(выбор осуществляется с помощью цифр)')
        hunting(game)


def exit_game(game):
    print('Спасибо за игру!')
    exit()#Для корректного закрытия приложения

def menu(game):
    # Тут выбор и ввод ответа в консоли
    print('Герой, вы попали в меню выберите из списка ниже и введите число вашего выбора')
    choice = input("1: Просмотр характеристик \n2: Поход к торговцу \n3: Охота на монстров \n4: Выход из игры\n")
    if choice == '1':
        character_stats(game)
    elif choice == '2':
        shopping(game)
    elif choice == '3':
        hunting(game)
    elif choice == '4':
        exit_game(game)
    else:
        print("НЕПРАВИЛЬНЫЙ ВЫБОР, выберите из списка и введите число!")
        menu(game)


game = open_save()
menu(game)
