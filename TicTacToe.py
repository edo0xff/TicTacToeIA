# TicTacToe Neural Network
# Eduardo B <eduardo@root404.com>

import BackPropagation
import Player
import GameBoard
import GameRegister

#Crea una red neuronal de 9 entradas 9 salidas
neuralNetwork = BackPropagation.NN(9, 9, 9)
#prepara el tablero
board = GameBoard.Board()
#para el registro de movimientos
register = GameRegister.Register()

# Entrena a la red neuronal con las jugadas realizadas
def Learn():
    global neuralNetwork
    global register

    train = raw_input("\n Do I need to train more? (y/n): ")

    if train == "y":
        print "\n Training with %s movements madafaka..." % (register.Len())
        neuralNetwork.train(register.GetGame())

def Play():
    global neuralNetwork
    global register
    global board

    board.Print()

    while True:

        P1Move = p1.GetMove(board, neuralNetwork)
        board.Set(P1Move, 1)

        mov = board.GetLastMovement()
        inverted  = [board.InvertBoard(mov[0]), board.InvertBoard(mov[1])]

        register.SaveMovement(inverted)

        board.Print()

        if board.IsWinner(1):
            print "\n Player 1 won"
            Learn()
            return

        elif board.IsFull():
            print "\n Draw"
            Learn()
            return

        P2Move = p2.GetMove(board, neuralNetwork)
        board.Set(P2Move, -1)

        register.SaveMovement(board.GetLastMovement())

        board.Print()

        if board.IsWinner(-1):
            print "\n Player 2 won"
            Learn()
            return

        elif board.IsFull():
            print "\n Draw"
            Learn()
            return

while True:

    print ""
    print "1) Human vs Human"
    print "2) Human vs IA"

    op = int(raw_input("\n Choose (1/2): "))

    if op == 1:
        p1 = Player.Human()
        p2 = Player.Human()

    else:

        first = raw_input("\n What do you want? (x/o): ")

        if first == "x":
            p1 = Player.Human()
            p2 = Player.IA()
        else:
            p1 = Player.IA()
            p2 = Player.Human()

    board.Drop()
    Play()
