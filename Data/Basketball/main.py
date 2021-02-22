"""
Создайте программу, хранящую информацию о великих баскетболистах.
Нужно хранить ФИО баскетболиста, его рост.
Требуется реализовать возможность добавления, удаления, поиска, замены данных.
Используйте словарь для хранения информации.
"""
from functions import line, is_float, input_float, input_str, input_int


def show_players(players):
    print('\n\n-----== Players ==----\n')
    for player in players:
        line()
        print(player_info(player))
    line()


def add_player_menu(players):
    print('--= Add player =--')
    player = {
        'surname': input_str('Surname: ', 2, 50),
        'name': input_str('Name: ', 2, 40),
        'middle_name': input_str('Middle name: ', 2, 50),
        'height': input_float('Height: ')
    }
    players.append(player)


def choose_player_menu(players):
    print('---= Choose player:')
    print('0 - back')
    for i, player in enumerate(players):
        print(f"{i + 1} - {player_info(player)}")
    choice = input_int('Choose number: ', 0, len(players))
    if choice == 0:
        return
    index = choice - 1
    player = players[index]
    edit_player_menu(player, players)


def player_info(player):
    """
    :param player: player
    :return: str
    'Bobenko Bob Bobovich (180 cm)'
    """
    return f"{player['surname']} {player['name']} {player['middle_name']} ({player['height']} cm)"


def edit_player_menu(player, players):
    while True:
        text = '--= Edit menu =--\n' \
               f'{player_info(player)}\n' \
               '0 - back\n' \
               '1 - edit surname\n' \
               '2 - edit name\n' \
               '3 - edit middle name\n' \
               '4 - edit height\n' \
               '5 - delete'
        print(text)
        choice = input('Your choice: ')
        if choice == '0':
            return
        elif choice == '1':
            player['surname'] = input_str('Input new surname: ', 2, 50)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        else:
            pass


def main_menu(players):
    while True:
        text = '--= Main menu =--\n' \
               '1 - add player\n' \
               '2 - find player\n' \
               '3 - edit\n' \
               '4 - show players\n' \
               '5 - exit'
        print(text)
        choice = input('Your choice: ')
        if choice == '1':
            add_player_menu(players)
        elif choice == '2':
            pass
        elif choice == '3':
            choose_player_menu(players)
        elif choice == '4':
            show_players(players)
        elif choice == '5':
            break
        else:
            pass
        print('\n\n\n')


def main():
    players = [
        {
            'surname': 'Bobenko',
            'name': 'Bob',
            'middle_name': 'Bobovich',
            'height': 190
        },
        {
            'surname': 'Bibenko',
            'name': 'Bib',
            'middle_name': 'Bibovich',
            'height': 175
        },
        {
            'surname': 'Bobanivna',
            'name': 'Boba',
            'middle_name': 'Bobivna',
            'height': 210
        }
    ]
    main_menu(players)


main()
