# quattro_tp_board.py
# Two player edition of Quattro (board utils in this file)

from time import *

# 'Quattro' - a clone of chess

player1_piece = 'Φ' # player's piece
player2_piece = 'τ' # computer's piece

#### Some functions I need ####
def prompt(text):
    '''a prompt skeleton'''
    val = input(text)
    return True if val not in ['0', 'N', 'n']  else False

def create_map(coords, dir_dict, direction = 'up'):
    '''creates a map of coordinates in front of the given coords and puts them
    in the dictionary 'dir_dict' (refer line no. 131 for an example)'''
    ## some requisite variables
    increment = 0
    if direction == 'up':
        increment = -1
    else:
        increment = 1
    (dir_dict['front'], dir_dict['left'],
     dir_dict['right'], dir_dict['diag-left'],
     dir_dict['diag-right']) =((coords[0], coords[1] + increment),
                               (coords[0]+increment, coords[1]), (coords[0] - increment, coords[1]),
                               (coords[0]+increment, coords[1]+increment), (coords[0] - increment, coords[1]+increment))
    ## Filtering invalid coordinates
    for i, j in dir_dict.items():
        for val in j:
            if val <0 or val >7:
                dir_dict[i] = None
                break
    return dir_dict
    


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
        return self.table[coords[1]][coords[0]]
    
    def crossover(self, coord, turn = 'player1'):
         '''executes the move 'cross over' for the required player, if necessary'''
         do_crossover = prompt("Do you want to cross over? (Y|N)")
         passed = False
         dirs = {'front':None, 'left':None, 'right': None, 'diag-left':None, 'diag-right':None} # directiosn before the piece
         if do_crossover:
            if turn == 'player1':
                dirs = create_map(coord, dirs)
                sides_check = [(self.get_piece(dirs['left']) if dirs['left'] != None else None)  == player2_piece,
                               (self.get_piece(dirs['right'])if dirs['right'] != None else None) == player2_piece]
                front_check = (self.get_piece(dirs['front']) if dirs['front'] != None else None) == player2_piece
                diagonal_check = [(self.get_piece(dirs['diag-left']) if dirs['diag-left'] != None else None) == 0,
                                  (self.get_piece(dirs['diag-right'])if dirs['diag-right'] != None else None) == 0]
                places = ['diag-left','diag-right']
                available = []
                for i in range(len(diagonal_check)):
                    if (diagonal_check[i] and sides_check[i]) and front_check:
                        available.append(places[i])
                print("You can cross over to the following coordinates:")
                for direction in available:
                    print("[" + str(available.index(direction)) + "]:" + str(dirs[direction]))
                index = input("Index no(Type 'None' if no coords are in the list):")
                move_coords  = dirs[available[eval(index)]] if eval(index) != None else None
                passed = True if eval(index)!= None else False
                if passed:
                    self.table[move_coords[1]][move_coords[0]] = player1_piece 
                    self.table[coord[1]][coord[0]] = 0
                return passed
            else:
                dirs = create_map(coord, dirs, direction = 'down')
                sides_check = [(self.get_piece(dirs['left']) if dirs['left'] != None else None)  == player1_piece,
                               (self.get_piece(dirs['right'])if dirs['right'] != None else None) == player1_piece]
                front_check = (self.get_piece(dirs['front']) if dirs['front'] != None else None) == player1_piece
                diagonal_check = [(self.get_piece(dirs['diag-left']) if dirs['diag-left'] != None else None) == 0,
                                  (self.get_piece(dirs['diag-right'])if dirs['diag-right'] != None else None) == 0]
                places = ['diag-left','diag-right']
                available = []
                for i in range(len(diagonal_check)):
                    if (diagonal_check[i] and sides_check[i]) and front_check:
                        available.append(places[i])
                print("You can cross over to the following coordinates:")
                for direction in available:
                    print("[" + str(available.index(direction)) + "]:" + str(dirs[direction]))
                index = input("Index no(Type 'None' if no coords are in the list):")
                move_coords  = dirs[available[eval(index)]] if eval(index) != None else None
                passed = True if eval(index)!= None else False
                if passed:
                    self.table[move_coords[1]][move_coords[0]] = player2_piece
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

