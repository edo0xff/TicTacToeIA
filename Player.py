class Human:

    def GetMove(self, Board, NeuralNetwork):
        while True:
            UserInput = int(raw_input("\n Put on: "))

            if Board.IsEmpty(UserInput):
                return UserInput

            else:
                print " Invalid!!!"


class IA:

    def GetMove(self, Board, NeuralNetwork):
        PossibleMoves = NeuralNetwork.test(Board.Get())

        for i in range(0, len(PossibleMoves), 1):

            MinVal = min(PossibleMoves)
            Index = PossibleMoves.index(MinVal) + 1

            if Board.IsEmpty(Index):
                return Index

            else:
                PossibleMoves[Index-1] = 1000
