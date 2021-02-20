import random
import sys
import time
import ja

# Gamefield
# u1|u2|u3
# m1|m2|m3
# l1|l2|l3
gamefield = [["ー", "ー", "ー"], ["ー", "ー", "ー"], ["ー", "ー", "ー"]]
u1 = gamefield[0][0]
u2 = gamefield[0][1]
u3 = gamefield[0][2]
m1 = gamefield[1][0]
m2 = gamefield[1][1]
m3 = gamefield[1][2]
l1 = gamefield[2][0]
l2 = gamefield[2][1]
l3 = gamefield[2][2]
maru = "〇"
batsu = "× "

# For judging input values
player_select_list = ["1", "2"]
point = 0
input_number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
input_item = 0
turn_action_record = [0]
j = 0


def game_view():
    """Game Field Drawing

    Draw the game screen on the CLI.
    """
    print(u1, u2, u3)
    print(m1, m2, m3)
    print(l1, l2, l3)


def myTurn(point: int, player_turn: int):
    """Player Turn Action

    A function of game progress on the player side.

    Args:
        point: An integer where to mark on the game field.
        player_turn: An integer indicating the first / second attack.
    """
    global j, input_item
    time.sleep(0.5)
    print(ja.player_turn_message)
    time.sleep(0.2)
    print(ja.instract_input_number_message)
    while point in turn_action_record:
        if j == 1:
            print(ja.entered_place_message)
        input_item = input(ja.prompt_cursor)
        while input_item not in input_number_list:
            print(ja.valid_number_message)
            input_item = input(ja.prompt_cursor)
        point = int(input_item)
        j = 1
    j = 0
    if point not in turn_action_record:
        turn_action_record.append(point)
        draw(point, player_turn)


def enemyTurn(point: int, player_turn: int):
    """Enemy Turn Action

    A function of game progress on the computer side.

    Args:
        point: An integer where to mark on the game field.
        player_turn: An integer indicating the first / second attack.
    """
    time.sleep(0.5)
    print(ja.computer_turn_notice)
    while point in turn_action_record:
        point = random.randint(1, 9)
    if point not in turn_action_record:
        turn_action_record.append(point)
        draw(point, player_turn)


def draw(point: int, player_turn: int):
    """Game Action

    Substitute 〇 or × in the game field list.
    In addition, a victory judgment is made.

    Args:
        point: An integer where to mark on the game field.
        player_turn: An integer indicating the first / second attack.
    """
    global u1, u2, u3, m1, m2, m3, l1, l2, l3
    global item
    item = ""
    # Turn
    if player_turn == 0:
        item = maru
    elif player_turn == 1:
        item = batsu
    # Game Parts Drawing
    if point == 1:
        u1 = item
    elif point == 2:
        u2 = item
    elif point == 3:
        u3 = item
    elif point == 4:
        m1 = item
    elif point == 5:
        m2 = item
    elif point == 6:
        m3 = item
    elif point == 7:
        l1 = item
    elif point == 8:
        l2 = item
    elif point == 9:
        l3 = item
    else:
        print(ja.error_message)
    game_view()
    # winning decision
    if u1 == u2 == u3 == item:
        win_judge(item)
    elif m1 == m2 == m3 == item:
        win_judge(item)
    elif l1 == l2 == l3 == item:
        win_judge(item)
    elif u1 == m1 == l1 == item:
        win_judge(item)
    elif u2 == m2 == l2 == item:
        win_judge(item)
    elif u3 == m3 == l3 == item:
        win_judge(item)
    elif u1 == m2 == l3 == item:
        win_judge(item)
    elif u3 == m2 == l1 == item:
        win_judge(item)


# WIN messages
def win_judge(item: str):
    """WIN messages

    Display a victory message and end the game.

    Args:
        item = A character string that stores 〇 or ×.
    """
    time.sleep(0.5)
    if item == maru:
        print(ja.win_message_maru)
        sys.exit()
    elif item == batsu:
        print(ja.win_message_batsu)
        sys.exit()


# Game Opening
print(ja.opening_message)
time.sleep(0.5)
input_item = input(ja.select_turn_message)
while input_item not in player_select_list:
    print(ja.select_player_error_message)
    input_item = input(ja.prompt_cursor)
turn = int(input_item)
if turn == 1:
    print(ja.start_first_message)
elif turn == 2:
    print(ja.start_second_message)
else:
    print(ja.wrong_input_message)
    sys.exit()
game_view()

# Game progression
for i in range(1, 6):
    player_turn = 0
    time.sleep(0.5)
    print(ja.turn_ + str(i))
    if turn == 1:
        myTurn(point, player_turn)
    elif turn == 2:
        enemyTurn(point, player_turn)
    if i == 5:
        print(ja.draw_message)
        sys.exit()
    player_turn = 1
    if turn == 1:
        enemyTurn(point, player_turn)
    elif turn == 2:
        myTurn(point, player_turn)
