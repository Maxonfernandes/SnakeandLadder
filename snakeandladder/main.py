import random

a, b, c, d = 0, 0, 0, 0
ladders = {3: 22, 5: 8, 11: 26, 20: 29, 17: 4}
snakes = {27: 1, 21: 9, 19: 7, 16: 3, 13: 5}

def move(pos):
    die = random.randint(1, 6)
    print(f"Rolled a {die}")
    new_pos = pos + die
    if new_pos > 100:
        print(f"Oops! You need {100 - pos} to win. Stay at {pos}")
        return pos
    if new_pos in snakes:
        print(f'Bitten by a snake! Slide down from {new_pos} to {snakes[new_pos]}')
        new_pos = snakes[new_pos]
    elif new_pos in ladders:
        print(f'Climb a ladder! Move up from {new_pos} to {ladders[new_pos]}')
        new_pos = ladders[new_pos]
    return new_pos

def playerturn(name, pos):
    print(f'\nPlayer {name}\'s turn (Current position: {pos})')
    chance = input('Enter x to roll the dice: ')
    if chance.lower() == 'x':
        new_pos = move(pos)
        print(f'Player {name} moved from position {pos} to {new_pos}')
        return new_pos
    return pos

def printboard():
    board = [['' for _ in range(10)] for _ in range(10)]
    players = {'A': a, 'B': b, 'C': c, 'D': d}

    # Fill the board with numbers
    for i in range(100):
        row = 9 - i // 10
        col = i % 10 if row % 2 == 0 else 9 - i % 10
        board[row][col] = f"{i+1:2d}"

    # Add players to the board
    for player, pos in players.items():
        if 0 < pos <= 100:
            row = 9 - (pos - 1) // 10
            col = (pos - 1) % 10 if row % 2 == 0 else 9 - (pos - 1) % 10
            board[row][col] += player

    print("\nCurrent Board:")
    print("-" * 41)
    for row in range(10):
        for col in range(10):
            print(f"|{board[row][col]:3}", end="")
        print("|")
        print("-" * 41)

def playgame():
    global a, b, c, d
    while max(a, b, c, d) < 100:
        a = playerturn('A', a)
        printboard()
        if a >= 100:
            print('Player A wins!')
            break
        b = playerturn('B', b)
        printboard()
        if b >= 100:
            print('Player B wins!')
            break
        c = playerturn('C', c)
        printboard()
        if c >= 100:
            print('Player C wins!')
            break
        d = playerturn('D', d)
        printboard()
        if d >= 100:
            print('Player D wins!')
            break

playgame()
