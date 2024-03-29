import quattro_tp_main as qtm
from quattro_tp_connector import *
### Designer printing
print("  #######  ##     ##    ###    ######## ######## ########   ####### ") 
print(" ##     ## ##     ##   ## ##      ##       ##    ##     ## ##     ##") 
print(" ##     ## ##     ##  ##   ##     ##       ##    ##     ## ##     ##") 
print(" ##     ## ##     ## ##     ##    ##       ##    ########  ##     ## ")
print(" ##  ## ## ##     ## #########    ##       ##    ##   ##   ##     ## ")
print(" ##    ##  ##     ## ##     ##    ##       ##    ##    ##  ##     ## ")
print("  ##### ##  #######  ##     ##    ##       ##    ##     ##  #######  ")
print("*"*68)
print()                  
print(" __  __ _____ _   _ _   _ ")
print("|  \/  | ____| \ | | | | |")
print("| |\/| |  _| |  \| | | | |")
print("| |  | | |___| |\  | |_| |")
print("|_|  |_|_____|_| \_|\___/ ")


print()
print()
###########
## Some functions
###########
def extract_from_file(txt_file):
    'extracts text data from text file "txt_file"'
    data = None
    try:
        with open(txt_file, 'r') as file:
            data = file.readlines()
    except:
        print("Oops! File not available!")
    return data

def menu():
    print("[1] START GAME")
    print("[2] GAME RULES")
    print("[3] VIEW CURRENT SCORES")
    print("[4] REGISTER USER")
    print("[5] VIEW PREVIOUS SCORES")
    print("[6] CREADITS")
    print("[0] EXIT GAME")

def enter_game():
    play_game = True
    while play_game:
        qtm.gameloop()
        play_game = qtm.qtp.prompt("Restart game? (Y|N)")
menu()
option=int(input("Enter your desired option: "))

while option !=0:
    if option ==1:
        print("You have chosen to play the game....")
        playerA = input("Enter @Player1 's name:")
        if not check_user(playerA):
            print("@auth::You hadn't registered before; but we'll register you as a newcomer.")
            try:
                register_user(playerA)
            except:
                print("A similar user exists, hence we allow you entry as that user.")
        playerB = input("Enter @Player2 's name:")
        if not check_user(playerB):
            print("@auth::You hadn't registered before; but we'll register you as a newcomer.")
            try:
                register_user(playerB)
            except:
                print("A similar user exists, hence we allow you entry as that user.")
        prev_scores_today = continue_today(playerA, playerB)
        if prev_scores_today != None:
            qtm.player1_score = prev_scores_today[0][0]
            qtm.player2_score = prev_scores_today[0][1]
        enter_game()
        match_save(playerA,playerB, [qtm.player1_score, qtm.player2_score])
    elif option == 2:
        print("You have chosen to view the game rules....")
        print("• While playing, one can move only one square at time.")
        print("• To move a piece, enter the coordinates of the piece according to the")
        print("  provided coordinates system ( in the format: x, y)")
        print("• One can conduct the “cross-over” move in the situations mentioned")
        print("  below.")
        print("• Let P denote the player piece and O denote the opponent piece")
        print()
        print("|   | O |   |          | P | O |   |")
        print("| O | P |   | ----->   | O |   |   |")
        print("|   |   |   |          |   |   |   |")
        print()
        print("|   | O |   |          |   | O | P |")
        print("|   | P | O | ----->   |   |   | O |")
        print("|   |   |   |          |   |   |   |")
        print()
        print("|   | O |   |          |   | O | P |        | P | O |   |")
        print("| O | P | O | ----->   | O |   | O |   or   | O |   | O |")
        print("|   |   |   |          |   |   |   |        |   |   |   |") 
    elif option == 3:
        print("Current score status:")
        try:
            print(f'@Player1({playerA})::',qtm.player1_score,f'\n@Player2({playerB})::',qtm.player2_score)
        except:
            print("You haven't started playing yet!")
    elif option == 4:
        finish = False
        while not finish:
            name = input("Name of the player(in less than 20 characters):")
            register_user(name)
            print("Registered successfully!")
            finish = not(qtm.qtp.prompt("Do you want to register more users?:"))
    elif option == 5:
        playerA = input("Enter @Player1 's name:")
        playerB = input("Enter @Player2 's name:")
        retrieve_scores(playerA, playerB)
    elif option == 6:
        credits = extract_from_file('E:\\Quattro v2\\Quattro-2\\credits.txt')
        if credits != None:
            for line in credits:
                print(line)
    else:
        print("Invalid option...")

    print()
    menu()
    option=int(input("Enter your desired option: "))
print("You have chosen to exit the game....")

