players = [''.join(item) for item in 'abcd']


def duck_duck_goose(players, goose):
    n = len(players)
    index = (goose - 1) % n
    return players[index].name


print(duck_duck_goose(players, 5))
