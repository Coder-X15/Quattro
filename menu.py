import quattro_tp_main as qtm

print("  #######  ##     ##    ###    ######## ######## ########   ####### ") 
print(" ##     ## ##     ##   ## ##      ##       ##    ##     ## ##     ##") 
print(" ##     ## ##     ##  ##   ##     ##       ##    ##     ## ##     ##") 
print(" ##     ## ##     ## ##     ##    ##       ##    ########  ##     ## ")
print(" ##  ## ## ##     ## #########    ##       ##    ##   ##   ##     ## ")
print(" ##    ##  ##     ## ##     ##    ##       ##    ##    ##  ##     ## ")
print("  ##### ##  #######  ##     ##    ##       ##    ##     ##  #######  ")
print()
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

def menu():
    print("[1] START GAME")
    print("[2] GAME RULES")
    print("[3] VIEW CURRENT SCORES")
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
        enter_game()
    elif option == 2:
        print("You have chosen to view the game rules....")
    elif option == 3:
        print("Current score status:")
        print("@Player1::",qtm.player1_score,"\n@Player2::",qtm.player2_score) 
    else:
        print("Invalid option...")

    print()
    menu()
    option=int(input("Enter your desired option: "))

print("You have chosen to exit the game....")

