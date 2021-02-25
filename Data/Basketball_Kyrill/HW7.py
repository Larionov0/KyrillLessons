"""
Создайте программу, хранящую информацию о великих баскетболистах.
Нужно хранить ФИО баскетболиста, его рост.
Требуется реализовать возможность добавления, удаления, поиска, замены данных.
Используйте словарь для хранения информации.
"""
from Funcs import line, is_float, input_float, input_str, input_int
import json

SAVING_FILENAME = 'players.json'


def save_data(players):
    file = open(SAVING_FILENAME, 'wt', encoding='utf-8')

    string_players = json.dumps(players, indent=4)
    file.write(string_players)

    file.close()


def load_data():
    file = open(SAVING_FILENAME, 'rt', encoding='utf-8')
    players = json.loads(file.read())
    file.close()
    return players


def try_to_load_data():
    try:
        players = load_data()
    except:
        players = [
            {
                'surname': 'Abra',
                'name': 'Abram',
                'middle_name': 'Abramovich',
                'height': 190.0
            },
            {
                'surname': 'Boba',
                'name': 'Boban',
                'middle_name': 'Bobovich',
                'height': 175.5
            },
            {
                'surname': 'Ciso',
                'name': 'Cisco',
                'middle_name': 'Ciscovich',
                'height': 210.0
            }
        ]
    return players


def show_players(players):
    print('\n---===   Players   ===---')
    for player in players:
        line()
        print(player_info(player))
    line()


def add_player_menu(players):
    print('\n---===   Add player   ===---')
    player = {
        'surname': input_str('Surname: ', 2, 30),
        'name': input_str('Name: ', 2, 30),
        'middle_name': input_str('Middle name: ', 2, 30),
        'height': input_float('Height: ')
    }
    players.append(player)


def choose_player_menu(players):
    print('\n---===   Choose player   ===---:')
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
    return f"{player['surname']} {player['name']} {player['middle_name']} ({player['height']} cm)"


def edit_player_menu(player, players):
    while True:
        text = '\n---===   Edit menu   ===---\n' \
               f'{player_info(player)}\n' \
               '0 - back\n' \
               '1 - edit surname\n' \
               '2 - edit name\n' \
               '3 - edit middle name\n' \
               '4 - edit height\n' \
               '5 - delete'
        print(text)
        choice = input('\nYour choice: ')
        if choice == '0':
            return
        elif choice == '1':
            player['surname'] = input_str('Input new surname: ', 2, 30)
        elif choice == '2':
            player['name'] = input_str('Input new name: ', 2, 30)
        elif choice == '3':
            player['middle_name'] = input_str('Input new middle name: ', 2, 30)
        elif choice == '4':
            player['height'] = input_float('Input new height: ')
        elif choice == '5':
            return players.remove(player)
        else:
            pass


def main_menu(players):
    while True:
        save_data(players)
        text = '\n---=== Main menu ===---\n' \
               '1 - add player\n' \
               '2 - find, edit player\n' \
               '3 - show players\n' \
               '4 - exit'
        print(text)
        choice = input('\nYour choice: ')
        if choice == '1':
            add_player_menu(players)
        elif choice == '2':
            choose_player_menu(players)
        elif choice == '3':
            show_players(players)
        elif choice == '4':
            break
        else:
            pass
        print('')


def main():
    players = try_to_load_data()
    main_menu(players)


main()
