def print_board(given_board):
    """
    Prints a board of x igul given the board list.
    :param given_board: A list of 3 list that represents the rows.
    :return: None
    """
    for line in given_board:
        # For line in board - board is a list of lists
        print(f"\t{line[0]}\t{line[1]}\t{line[2]}")


current_board = [['-', '-', '-'],
         ["-", "-", '-'],
         ["-", "-", "-"]]

choice_index = int(input("Please enter the index of the location"))

line_index = int(choice_index/3)
location_inside_line = choice_index%3

# Check if the location the user entered is empty:
# if board[line_index][location_inside_line] is not '-':
# print("Error! It is already taken, try other location")


#board[line_index][location_inside_line]
print("Hi! welcome to our game :)")

print("In order to input your choice, please enter the number of the index and then X or O")
insturction_board=[[0,1,2],[3,4,5],[6,7,8]]

print_board(insturction_board)


print_board(current_board)


"""
current_number_of_turns=0
while current_number_of_turns <= 9 :
    get user's input location
    change the board according to the location that the user entered
    print the new board
    winner = who_is_the_winner(board)
    if winner != None:
        print("Congratulations! {winner} won")
        break
    current_number_of_turns += 1
"""
def get_winner(board):
    winner = None
    if board[0][0]==board[1][1] and board[1][1] == board[2][2]:
        winner = board[0][0]
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        winner = board[0][2]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        winner = board[0][1]
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        winner = board[0][0]
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        winner = board[2][0]
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        winner = board[1][0]
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        winner = board[0][0]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        winner = board[0][2]

shura=input("please enter the shura: ")
amuda=input("please enter the amuda: ")





if winner != 'x' and winner != 'o':
    return None
    return winner

#my_board=[['x', 'o', 'o'],
        # ["o", "x", 'o'],
         #["o", "o", "x"]]

#winner = get_winner(my_board)
#print(f"the winner is:{winner}")

