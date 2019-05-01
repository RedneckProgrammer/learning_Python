"""" Tic tac toe game
The approach:

1. take user input
2. update board with user input
3. check for winner

board

      |   |
    1 | 2 |3
   ------------
      |   |
    4 | 5 |6
   ------------
    7 |  8|9
      |   |

    ask user to input number from 1-9 to put X or O
    save input to list
"""

board_as_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def win_check(a):
    if a[0] == 'X' and a[1] == 'X' and a[2] == 'X':
        return True, 'X'
    if a[3] == 'X' and a[4] == 'X' and a[5] == 'X':
        return True, 'X'
    if a[6] == 'X' and a[7] == 'X' and a[8] == 'X':
        return True, 'X'
    if a[0] == 'X' and a[3] == 'X' and a[6] == 'X':
        return True, 'X'
    if a[1] == 'X' and a[4] == 'X' and a[7] == 'X':
        return True, 'X'
    if a[2] == 'X' and a[5] == 'X' and a[8] == 'X':
        return True, 'X'
    if a[0] == 'X' and a[4] == 'X' and a[8] == 'X':
        return True, 'X'
    if a[2] == 'X' and a[4] == 'X' and a[6] == 'X':
        return True, 'X'
    if a[0] == 'O' and a[1] == 'O' and a[2] == 'O':
        return True, 'O'
    if a[3] == 'O' and a[4] == 'O' and a[5] == 'O':
        return True, 'O'
    if a[6] == 'O' and a[7] == 'O' and a[8] == 'O':
        return True, 'O'
    if a[0] == 'O' and a[3] == 'O' and a[6] == 'O':
        return True, 'O'
    if a[1] == 'O' and a[4] == 'O' and a[7] == 'O':
        return True, 'O'
    if a[2] == 'O' and a[5] == 'O' and a[8] == 'O':
        return True, 'O'
    if a[0] == 'O' and a[4] == 'O' and a[8] == 'O':
        return True, 'O'
    if a[2] == 'O' and a[4] == 'O' and a[6] == 'O':
        return True, 'O'


while True:

    board = """


    {0} | {1}  |{2}
     --------
    {3} | {4}  | {5} 
     --------
     {6}|  {7} | {8}  

    """.format(board_as_list[0], board_as_list[1], board_as_list[2], board_as_list[3], board_as_list[4],
               board_as_list[5],
               board_as_list[6], board_as_list[7], board_as_list[8])

    print(board)

    place_to_insert = input("Please enter number from 1-9 to place your X or O:  ")

    try:
        int(place_to_insert)
    except ValueError:
        print('You probably entered wrong values')
        continue

    marker_to_insert = input("X or O(letter not number):  ")

    if marker_to_insert == 'X':
        board_as_list[int(place_to_insert)-1] = 'X'
    elif marker_to_insert == 'x':
        board_as_list[int(place_to_insert) - 1] = 'X'
    elif marker_to_insert == 'O':
        board_as_list[int(place_to_insert)-1] = 'O'
    elif marker_to_insert == 'o':
        board_as_list[int(place_to_insert)-1] = 'O'
    else:
        print("'You probably entered wrong values'")
        continue

    #Win check defined above

    try:
        if win_check(board_as_list)[0]:
            print("Game over - {} won".format(win_check(board_as_list)[1]))
    except TypeError:
        continue






