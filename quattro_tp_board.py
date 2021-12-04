# quattro_tp_board.py
# Two player edition of Quattro (board utils in this file)

from time import *

# 'Quattro' - a clone of chess

player1_piece = 'Φ' # player's piece
player2_piece = 'τ' # computer's piece

def prompt(text):
    '''a prompt skeleton'''
    val = input(text)
    return True if val not in ['0', 'N', 'n']  else False

class InvalidMove(Exception):
    '''error when you/ the computer takes an invalid move'''
    def __init__(self, coord):
        self.message = "Invalid move at"
        self.coords = coord
        

class PlayTable:
    def __init__(self, table_side):
        ''' generates the game board, empty and with no pieces '''
        self.length = table_side
        self.table = [[0]*table_side]*table_side

    def __repr__(self):
        '''prints the table'''
        print()
        table_str = ''
        num = 0
        for row in self.table:
            table_str += str(num) + " \t"
            for piece in row:
                table_str += str(piece) + "|"
            table_str += "\n"
            num += 1
        return table_str + "\t0 1 2 3 4 5 6 7"
        
    def reset(self):
        ''' resets the board/ places pieces on it '''
        for row in [0, 1] :
            self.table[row] = [player2_piece]*self.length

        for row in [self.length-2, self.length - 1] :
            self.table[row] = [player1_piece]*self.length
        
        for row in range(2, self.length-2):
            self.table[row] = [0]*self.length
    def move_piece(self, coord, turn = 'player1'):
        '''moves the piece at coord '''
        if turn == 'player1' and self.table[coord[1]%self.length][coord[0]%self.length] in [player2_piece, 0]:
            raise InvalidMove(coord)
        elif turn == 'player2' and self.table[coord[1]%self.length][coord[0]%self.length] in [player1_piece,0]:
            raise InvalidMove(coord)
        elif self.table[coord[1]%self.length][coord[0]%self.length] != 0 and self.table[(coord[1] + (1 if turn == 'player2' else -1))%self.length][coord[0]%self.length] == 0:
            temp = self.table[coord[1]][coord[0]]
            self.table[coord[1]][coord[0]] = 0
            direction = 1 if turn == 'player2' else -1
            self.table[coord[1]+direction][coord[0]] = temp
            print(f"Moved {temp} from {(coord[0] if coord[0] >= 0 else 8 + coord[0],coord[1] if coord[1] >= 0 else 8 + coord[1])}") # msg
        else:
            raise InvalidMove(coord)
    def get_piece(self, coords):
        '''returns the piece at coords'''
        ## Handling out-of-range indices... a messy bit since we're going
        ## out of the way (i.e, using the indexing system rather the table's
        ## coordinate system)
        coords = list(coords)
        if coords[1] >= 7:
            coords[1] == 0
        if coords[1] < 0:
            coords[1] = 7
        if coords[0] >= 7:
            coords[0] == 0
        if coords[0] < 0:
            coords[0] = 7
        return self.table[coords[1]][coords[0]]
    
    def crossover(self, coord, turn = 'player1'):
         '''executes the move 'cross over' for the required player, if necessary'''
         do_crossover = prompt("Do you want to cross over? (Y|N)")
         passed = False
         if do_crossover:
            ## evaluate positions capable of crossing over to
            side_coords = [(coord[0] + 1, coord[1]), (coord[0]-1, coord[1])] # the boxes on either sides of the piece
            front_coord = (coord[0], coord[1] + (1 if turn == 'player2' else -1)) # the box in front
            ## (below) the diagonal spaces to evaluate
            diag_coords = {(coord[0] + 1, coord[1] + (1 if turn == 'player2' else -1)):False,(coord[0] - 1, coord[1] + (1 if turn == 'player2' else -1)):False} 
            is_enemy_in_front = True if self.get_piece(front_coord) == (player2_piece if turn == 'player1' else player1_piece)  else False
            is_diag_spc_0_empty = True if self.get_piece(list(diag_coords.keys())[0]) == 0 else False # is the diagonal space empty?? 
            is_diag_spc_1_empty = True if self.get_piece(list(diag_coords.keys())[1]) == 0 else False # is the diagonal space empty??
            ## Checking for the enemy in the right side and a possibility to corss over
            print("Piece at", side_coords[0], " is", self.get_piece(side_coords[0]))
            if is_diag_spc_0_empty and (is_enemy_in_front and self.get_piece(side_coords[0]) == (player2_piece if turn == 'player1' else player1_piece)):
                diag_coords.update({(coord[0] + 1, coord[1] + (1 if turn == 'player2' else -1)): True})
            ## Checking for the enemy in the left side and a possibility to corss over
            print("Piece at", side_coords[1], " is", self.get_piece(side_coords[1]))
            if is_diag_spc_1_empty and (is_enemy_in_front and self.get_piece(side_coords[1]) == (player2_piece if turn == 'player1' else player1_piece)):
                diag_coords.update({(coord[0] - 1, coord[1] + (1 if turn == 'player2' else -1)):True})
            movable = []
            print("You can cross over to the following coordinates:")
            for key, value in diag_coords.items():
                if value == True:
                    print(key)
                    movable.append(key)
                else:
                    pass
            print("Enter the index of the coords you wish to move to from the list:")
            for i in range(len(movable)):
                print("Index "+str(i), movable[i])
            index = input("Index no(Type 'None' if no coords are in the list):")
            move_coords  = movable[eval(index)] if eval(index) != None else None
            passed = True if eval(index)!= None else False
            if passed:
                self.table[move_coords[1]][move_coords[0]] = player1_piece if turn == 'player1' else player2_piece
                self.table[coord[1]][coord[0]] = 0
            return passed
    def check_victory(self, turn):
            '''checks if the person playing `turn` has won.
               Winning condition - at least four pieces on the enemy side's
               back row'''
            if turn == 'player1':
                if self.table[0].count(player1_piece) >= 4:
                    return 'player1'
            elif turn == 'player2':
                if self.table[7].count(player2_piece) >= 4:
                    return 'player2'
            else:
                return None
            
             
board = PlayTable(8) # creating the board object

