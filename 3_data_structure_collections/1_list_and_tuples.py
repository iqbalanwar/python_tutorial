'''
Lists are mutable
- Lists are an ordered collection
Tuples are not mutable
- Tuples are also an ordered collection
- They were exactly the same, but can't be modified
'''

def main():
    game_one_list()
    game_two_list()
    game_tuple()

def game_one_list():
    print("========== Game One List ==========")
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    i = game.index('Paper')
    print(f'{game[i]} is on index {i}')

    game.append('Computer')    # adds an item to the end of the list
    game.insert(0, 'Shotgun')  # inserts an item based on given index
    game.remove('Lizard')      # removes an item based on the first matching value
    game.pop()                 # removes an item at the end of the list

    x = game.pop() # pop can also return the popped value
    # using pop and append together can simulate a stack
    game.pop(0);   # pop also removes based on index
    print(f'{x} was popped')

    print_list(game)

def game_two_list():
    print("========== Game Two List ==========")
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(', '.join(game)) # Prints the list, with commas between
    print_list(game)       # Prints the list as is
    print('The length of game is {}'.format(len(game)))

def game_tuple():
    print("========== Game Tuple ==========")
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    print(', '.join(game))  # Prints the list, with commas between
    print_list(game)       # Prints the list as is
    print('The length of game is {}'.format(len(game)))

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
