import quattro_tp_board as qtp

#########################
## Some variables to begin with
#########################
player1_score = 0
player2_score = 0
auto_moves = [(5,6),(4,1),(5,5),(4,2),(5,4),(4,3),(5,3),(4,4),(5,7),(6,1),(5,2),(5,1),(5,6),(4,5),(5,5),(5,6),(5,4),(6,2),(5,3),(5,0),
              (6,1),(7,1),(6,2),(7,0),(6,1),(3,1),(4,6),(3,0),(4,5),(3,2),(4,4),(2,1),(4,3),(5,2),(4,2),(5,3),(4,1),(5,4),(2,6),(1,1),
              (2,5),(1,0),(2,4),(1,2),(2,3),(3,1),(1,2),(0,1),(2,1)]

def gameloop():
    qtp.board.reset()
    is_auto = qtp.prompt("Autoplay on/off?? (Y|N)")
    i  = 0 # a counter to look up whose turn it is
    print(qtp.board)    
    while True:
        print('-'*21) # decorations
        # infinite loop here till errors occur
        all_gone_good = True
        player1_mv = eval(input("@Player1::Enter your move:")) if (i > len(auto_moves)-1 and is_auto) or not is_auto else auto_moves[i]  # waiting for the first player's move        
        i += 1
        try:
            # for player 1 to try and move
            qtp.board.move_piece(player1_mv, turn = 'player1')
        except qtp.InvalidMove:
            # handling an invalid move
            if qtp.board.get_piece(player1_mv) == qtp.player1_piece and qtp.board.table[player1_mv[1]-1][player1_mv[0]] == qtp.player2_piece:
                # checking chances of crossover
                all_gone_good = qtp.board.crossover(player1_mv, turn = 'player1')
            else:
                print("Invalid move at",player1_mv)
                all_gone_good = False 
        except IndexError:
            print("You can't move a piece at an end!")
            all_gone_good = False
        except TypeError or ValueError:
            print("The coordinates of the piece to be moved is invalid")
            all_gone_good = False
        if qtp.board.check_victory('player1') == 'player1':
            print("The winner is @Player1!")
            global player1_score
            player1_score += 1
            break
        # next we check if the player's move was valid and then
        # allow player 2 to play if all had gone well
        print('-'*21) # decorations 
        if all_gone_good:
            print(qtp.board)
            all_gone_good = False
            while not all_gone_good:
                player2_mv = eval(input("@Player2::Enter your move:"))if (i > len(auto_moves)-1 and is_auto) or not is_auto else auto_moves[i] # waiting for the second player's move
                try:
                    # for player 2
                    qtp.board.move_piece(player2_mv, turn = 'player2') 
                    print(qtp.board)
                    all_gone_good = True
                except qtp.InvalidMove:
                    if qtp.board.get_piece(player2_mv) == qtp.player2_piece and qtp.board.table[player2_mv[1]+1][player2_mv[0]] == qtp.player1_piece:
                        all_gone_good = qtp.board.crossover(player2_mv, turn = 'player2')
                    else:
                        print("Invalid move at",player2_mv)
                        all_gone_good = False
                except IndexError:
                        print("You can't move a piece at an end!")
                        all_gone_good = False
                except TypeError or ValueError:
                        print("The coordinates of the piece to be moved is invalid")
                        all_gone_good = False
        i += 1
        if qtp.board.check_victory('player2') == 'player2':
            print("The winner is @Player2!")
            global player2_score
            player2_score += 1
            break
    print("Scoreboard")
    print("@Player1::", player1_score,"\n@Player2::", player2_score)
