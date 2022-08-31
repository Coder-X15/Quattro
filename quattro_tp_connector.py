import mysql.connector as sql
##########
## Connectivity
##########
### Just putting comments to keep track of the uses and to make sure I have done them right
save_utils = sql.connect(host = "localhost", user = 'root', passwd = 'sh3rl0c')
save_utils.autocommit = True # to help save changes automatically. Usually this switch is False
save_cursor = save_utils.cursor() # the cursor to navigate through data and to execute commands
save_cursor.execute("create database if not exists Quattro;") # creates the database to save game data
save_cursor.execute("use Quattro;") # uses the database
save_cursor.execute("create table if not exists user_registry(user_name varchar(20) unique, join_date date);") # creates the user registry in the DB

def match_save(player1_name, player2_name, scores):
    '''Saves the match scores'''
    #### Creates the match scores table first, then inserts the values into it
    save_cursor.execute(f'create table if not exists {player1_name}vs{player2_name}(matchday date primary key, {player1_name} int, {player2_name} int);')
    try:
        save_cursor.execute(f'insert into {player1_name}vs{player2_name} values(current_date(), {scores[0]},{scores[1]});')
    except:
        save_cursor.execute(f'update {player1_name}vs{player2_name} set {player1_name} = {scores[0]}, {player2_name} = {scores[1]} where matchday = current_date();')

def register_user(username):
    '''registers the user into the user_registry'''
    save_cursor.execute(f'insert into user_registry values("{username}",current_date());')
    
def check_user(username):
    '''checks if username has been registered'''
    save_cursor.execute('select user_name from user_registry')
    list_of_users = save_cursor.fetchall()
    return ((username,) in list_of_users)
