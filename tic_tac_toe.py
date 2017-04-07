#

current_positions = {"top left": " ", "top center": " ",
"top right": " ","center left": " ", "center": " ", "center right": " ",
"bottom left": " ", "bottom center": " ", "bottom right": " "}


current_player = "X"


some_string = "Hello {a_value}, {some_value}".format(a_value = "x", some_value = "y")
print some_string



print "\nANOTHER WAY: Using a Dictionary\n"

some_dictionary = {"a_value" : "x", "some_value" : "y"}
some_string = "Hello {a_value}, {some_value}".format(**some_dictionary)
print some_string



def display_board(current_positions):
    board = """
    {top left} | {top center} | {top right}
    ---------
    {center left} | {center} | {center right}
    ---------
    {bottom left} | {bottom center} | {bottom right}
    """.format(**current_positions)
    print board

def user_move(current_positions, current_player):
    possible_moves = []
    user_prompt = "Please pick your move from the options below."
    for position in current_positions:
        if current_positions[position] == " ":
            possible_moves.append(position)
            user_prompt += "\n" + position
    user_prompt += "\n"
    user_choice = raw_input(user_prompt).lower()
    while user_choice not in possible_moves:
        user_choice = raw_input(user_prompt).lower()
    current_positions[user_choice] = current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return current_positions, current_player


def is_game_over(current_positions):
    winners = [[],
    [],
    [],
    [],
    [],
    [],
    [],
    []]


current_positions, current_player = user_move(current_positions, current_player)
print current_player
display_board(current_positions)
