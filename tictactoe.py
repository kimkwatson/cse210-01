# Tic Tac Toe W02
# Author Kim Watson

def main():
    
    x_wins = 0
    o_wins = 0
    draws = 0
    x_turns = 0
    o_turns = 0

    is_playing = True

    print()
    print("Welcome to Tic Tac Toe\n")

    # Call set_grid_dict function to create a tic tac toe grid and save it as a dictionary.
    grid_dictionary = set_grid_dict()
    
    # Call display_grid function to print the grid to screen.
    display_grid(grid_dictionary)

    while is_playing:

        while x_turns < 5:
            
            # Call prompt_x function to retrieve square choice from player X.
            prompt_x(grid_dictionary)

            # Call display_grid function to display updated grid.
            display_grid(grid_dictionary)
            
            # Determine if X has won.
            if determine_status(grid_dictionary) == "over":
                winner = "X"
                x_wins += 1
                break
            else:
                x_turns += 1

            if o_turns < 4:
                # Call prompt_o function to retrieve square choice from player O.
                prompt_o(grid_dictionary)

                # Call display_grid function to display updated grid.
                display_grid(grid_dictionary)

                # Determine if Y has won.
                if determine_status(grid_dictionary) == "over":
                    winner = "O"
                    o_wins += 1
                    break
                else:
                    o_turns += 1
        else:
            winner = "none"
            draws += 1

        # Call display_gameover_message to display results of the game.
        display_gameover_message(winner, x_wins, o_wins, draws)

        # Call opt_in function to ask user whether or not to continue and update is_playing boolean.
        is_playing = opt_in()

        if is_playing:
            # Call functions again to reset grid for a new game and print to screen.
            grid_dictionary = set_grid_dict()
            display_grid(grid_dictionary)
            x_turns = 0
            o_turns = 0

    print()
    print("Thank you for playing Tic Tac Toe")
    print()

def set_grid_dict():

    grid_dictionary = {1: "1", 2: "2", 3: "3", 4: "4", 5:"5", 6: "6", 7: "7", 8: "8", 9: "9"}
    return grid_dictionary

def prompt_x(grid):

    square = input("\nX's turn to choose a square (1-9): ")
    if square.isnumeric():
        square = int(square)
        if square >= 1 and square <= 9:
            grid[square] = "X"
        else:
            print("Not a valid option. Please try again.")
            prompt_x(grid)

    else:
        print("Not a valid option. Please try again.")
        prompt_x(grid)

    return grid
    
def prompt_o(grid):

    square = input("\nO's turn to choose a square (1-9): ")
    if square.isnumeric():
        square = int(square)
        if square >= 1 and square <= 9:
            grid[square] = "O"
        else:
            print("Not a valid option. Please try again.")
            prompt_o(grid)

    else:
        print("Not a valid option. Please try again.")
        prompt_o(grid)
    return grid

def display_grid(grid):
    
    print()
    print(f"{grid[1]}|{grid[2]}|{grid[3]}")
    print("-+-+-")
    print(f"{grid[4]}|{grid[5]}|{grid[6]}")
    print("-+-+-")
    print(f"{grid[7]}|{grid[8]}|{grid[9]}")

def determine_status(grid):

    if grid[1] == grid[2] and grid[2] == grid[3]:
        status = "over"

    elif grid[4] == grid[5] and grid[5] == grid[6]:
        status = "over"

    elif grid[7] == grid[8] and grid[8] == grid[9]:
        status = "over"
    
    elif grid[1] == grid[4] and grid[4] == grid[7]:
        status = "over"

    elif grid[2] == grid[5] and grid[5] == grid[8]:
        status = "over"

    elif grid[3] == grid[6] and grid[6] == grid[9]:
        status = "over"
    
    elif grid[1] == grid[5] and grid[5] == grid[9]:
        status = "over"

    elif grid[7] == grid[5] and grid[5] == grid[3]:
        status = "over"

    else:
        status = "not over"

    return status

def display_gameover_message(winner, x_wins, o_wins, draws):

    print()
    if winner == "X":
        message = "Game Over. X's Win!"

    elif winner == "O":
        message = "Game Over. O's Win!"

    else:
        message = "Game Over. It's a Draw."

    print(message)
    print()
    print(f"X: {x_wins}\tO: {o_wins}\tDraws: {draws}")

def opt_in():

    play = input("\nWould you like to play again (Y?N)? ")

    if play.lower() == "y" or play.lower() == "yes":
        is_playing = True

    else:
        is_playing = False

    return is_playing

# Call main to start this program.
if __name__ == "__main__":
    main()