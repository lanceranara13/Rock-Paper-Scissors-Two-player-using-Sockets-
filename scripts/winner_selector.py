
# 0 = rock
# 1 = paper
# 2 = scissors
# 3 = player 1
# 4 = player 2
# 5 = draw
def numberAssign(a):
    a = str(a)
    if(a == "rock"):
        return 0
    elif(a == "paper"):
        return 1
    elif(a == "scissors"):
        return 2

def winner(a, b):

    a = int(numberAssign(a))
    b = int(numberAssign(b))

    if(a == b):
        return 5
    elif(a == 0 and b == 1):
        return 4
    elif(a == 1 and b == 2):
        return 4
    elif(a == 1 and b == 0):
        return 3
    elif(a == 2 and b == 1):
        return 3
    elif(a == 0 and b == 2):
        return 3
    elif(b == 0 and a == 2):
        return 4
    return 5


# if __name__ == '__main__':