def print_grid(some_grid):
    if isinstance(some_grid, str):
        print('---------')
        for i in range(0, 9, 3):
            print('|', end=' ')
            print(' '.join(some_grid[i:i + 3]).replace('_', ' '), end=' |\n')
        print('---------')
    elif isinstance(some_grid, list):
        print('---------')
        for row in some_grid:
            print('|', ' '.join(row).replace('_', ' '), "|")
        print('---------')


def string_grid_to_list(str_grid):
    list_grid = list(str_grid)

    # Convert flat list to 2D list
    return [list_grid[i:i+3] for i in range(0, 9, 3)]


def has_consecutive_three(grid, player):
    """
    Check if a player has three consecutive markers in the 3x3 grid.

    :param list grid: 3x3 game board.
    :param str player: Marker ('X' or 'O').
    :return: True if a win condition is met, else False.
    :rtype: bool
    """

    # Check rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] == player:
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] == player:
            return True

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True

    return False


def has_empty_cells(grid):
    """
    Check if the 3x3 grid contains any empty cells represented by ' ' or '_'.
    :param grid: 3x3 list representing the game board.
    :return: True if there are any empty cells, otherwise False.
    """
    return any([grid[i][j] in (' ', '_') for i in range(3) for j in range(3)])


def count_player_marks(grid, player):
    """Count the number of marks for a given player in the grid."""
    return sum(1 for i in range(3) for j in range(3) if grid[i][j] == player)


def is_game_state_possible(grid):
    """
    Check if the game state is possible.

    A game state is impossible if:
    - Both players have three in a row.
    - The difference between X and O marks is more than 1.
    """

    if has_consecutive_three(grid, 'X') and has_consecutive_three(grid, 'O'):
        return False

    # Check the difference in marks
    if abs(count_player_marks(grid, 'X') - count_player_marks(grid, 'O')) > 1:
        return False

    return True


def is_game_finished(grid):
    # If any player has won
    if has_consecutive_three(grid, 'X') or has_consecutive_three(grid, 'O'):
        return True

    if not has_empty_cells(grid):
        return True

    return False


def print_game_status(grid):
    print(get_game_status(grid))


def get_game_status(grid):
    if not is_game_state_possible(grid):
        return 'Impossible'
    elif has_consecutive_three(grid, 'X'):
        return 'X wins'
    elif has_consecutive_three(grid, 'O'):
        return 'O wins'
    elif is_game_finished(grid):
        return 'Draw'
    else:
        return 'Game not finished'


def make_move(grid, player):
    while True:
        print('> ', end='')
        coordinates = input().split()
        try:
            i = int(coordinates[0]) - 1
            j = int(coordinates[1]) - 1
            if grid[i][j] not in (' ', '_'):
                print('This cell is occupied! Choose another one!')
                continue
            grid[i][j] = player
        except ValueError:
            print('You should enter numbers!')
            continue
        except IndexError:
            print('Coordinates should be from 1 to 3!')
            continue
        print_grid(grid)
        break

    return grid


# string_grid = input('> ')  # prompt the user to enter a game state in the form _XXOO_OX_
string_grid = '_________'  # start a new game with an empty grid
list_grid = string_grid_to_list(string_grid)
print_grid(string_grid)

game_status = get_game_status(list_grid)
player = 'X'

while game_status == 'Game not finished':
    list_grid = make_move(list_grid, player)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    game_status = get_game_status(list_grid)

print_game_status(list_grid)
