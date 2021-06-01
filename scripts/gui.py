from tkinter import *
from winner_selector import *
# from client import *
import socket

root = Tk()
root.title("Simple Rock Paper Scissors Game")


HOST = '127.0.0.1'
PORT = 65432
choice = "none"

def rock(submitButton, tex):
    print('0')
    global choice
    choice = 'rock'
    tex['text'] = "Your choice: " + choice
    submitButton['state'] = NORMAL
def paper(submitButton, tex):
    print('1')
    global choice
    choice = 'paper'
    tex['text'] = "Your choice: " + choice
    submitButton['state'] = NORMAL
def scissors(submitButton, tex):
    print('2')
    global choice
    choice = 'scissors'
    tex['text'] = "Your choice: " + choice
    submitButton['state'] = NORMAL
def submit(sckt, playerno, but):


    try:
        sckt.send(str.encode(choice))

        client_choice = sckt.recv(1024)
    except socket.error as e:
        print(e)


    gameend = Tk()
    canvas = Canvas(gameend, width=300, height=200).grid(columnspan=5, rowspan=2)

    print(choice, client_choice.decode())
    if(playerno == 1):
        winnerPlayer = winner(choice, client_choice.decode())-2
    else:
        winnerPlayer = winner(client_choice.decode(), choice)-2
    print(winnerPlayer)

    name = "Player "+str(playerno) + ": "
    if(winnerPlayer == 3):
        name = name + "Draw"
        gameend.title(name)
        winnerL = Label(gameend, text=name).grid(row=0, column=0)
    elif(playerno == winnerPlayer):
        name = name + "You win"
        gameend.title(name)
        winnerL = Label(gameend, text=name).grid(row=0, column=0)
    else:
        name = name + "You lose"
        gameend.title(name)
        winnerL = Label(gameend, text=name).grid(row=0, column=0)

    gameend.mainloop()





def server():
    global HOST
    if(ip.get() != ""):
        HOST = str(ip.get())
    root.quit()
    print(HOST)

    # waiting = Tk()
    # waitinglabel = Label(waiting, text="Waiting for another player...").grid(row=0, column=0)

    # waiting.mainloop()

    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.bind((HOST, PORT))
    s1.listen()
    clientsocket, address = s1.accept()

    # waiting.quit()

    player1 = Tk()
    player1.title("Player 1")

    canvas = Canvas(player1, width=300, height=300).grid(columnspan=5, rowspan=2)

    tex = Label(player1, text="Pick one:").grid(row=0, column=0)
    tex2 = Label(player1, text="Your choice: ")

    submitButton = Button(player1, text="Submit", state=DISABLED)
    submitButton['command'] = lambda:submit(clientsocket, 1, submitButton)

    rockButton = Button(player1, text="Rock", command=lambda:rock(submitButton, tex2))
    paperButton = Button(player1, text="Paper", command=lambda:paper(submitButton, tex2))
    scissorsButton = Button(player1, text="Scissors", command=lambda:scissors(submitButton, tex2))

    rockButton.grid(row=0, column=1)
    paperButton.grid(row=0, column=2)
    scissorsButton.grid(row=0, column=3)
    submitButton.grid(row=1, column=3)
    tex2.grid(row=1, column=1)




    player1.mainloop()








def client():
    global HOST
    if(ip.get() != ""):
        HOST = str(ip.get())
    root.quit()
    # create()
    root.quit()
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((HOST, PORT))

    player2 = Tk()
    player2.title("Player 2")

    canvas = Canvas(player2, width=300, height=300).grid(columnspan=5, rowspan=2)

    submitButton = Button(player2, text="Submit", state=DISABLED)
    submitButton['command'] = lambda:submit(s2, 2, submitButton)

    tex = Label(player2, text="Pick one:").grid(row=0, column=0)
    tex2 = Label(player2, text="Your choice: ")
    rockButton = Button(player2, text="Rock", command=lambda:rock(submitButton, tex2))
    paperButton = Button(player2, text="Paper", command=lambda:paper(submitButton, tex2))
    scissorsButton = Button(player2, text="Scissors", command=lambda:scissors(submitButton, tex2))

    # submitButton = Button(player2, text="Submit", command=submit(s2, 2), state=DISABLED)
    rockButton.grid(row=0, column=1)
    paperButton.grid(row=0, column=2)
    scissorsButton.grid(row=0, column=3)
    submitButton.grid(row=1, column=3)
    tex2.grid(row=1, column=1)
    player2.mainloop()





title = Label(root, text="IP: ").grid(row=0, column=0)
ip = Entry(root, width=50, borderwidth=5)

ip.grid(row=0, column=1)

hostButton = Button(root, text="Host Game", command=server).grid(row=1, column=0)
joinButton = Button(root, text="Join Game", command=client).grid(row=1, column=1)


root.mainloop()