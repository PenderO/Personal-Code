#from map import *

TILESIZE = 32

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        row = [int(item) for item in row]
        game_map.append(list(row))
    return game_map

'''def weird_load_map(path):
    with open(path + '.txt', 'r') as f:
        data = f.read().splitlines() # splitlines() is cleaner than split('\n')
    game_map = []
    for row in data:
        row_data = [int(item) for item in row.split()]
        game_map.append(row_data)
        
    return game_map'''
    
def other_load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    #data = data.split('\t')
    data = data.split()
    game_map = []
    for row in data:
        row = [int(item) for item in row]
        game_map.append(list(row))
    return game_map


game_map = other_load_map('mapfile')


COLS = 0
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        game_map[i][j] = int(game_map[i][j])
ROWS = len(game_map)
COLS = len(game_map[0])