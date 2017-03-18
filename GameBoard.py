class Board:

    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.prevState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def Set(self, index, value):
        self.prevState = self.Copy()
        self.board[index - 1] = value

    def Get(self):
        return self.board

    def GetLastMovement(self):
        return [self.prevState, self.board]

    def Drop(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.prevState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def IsFull(self):
        for value in self.board:
            if value == 0:
                return False

        return True

    def IsWinner(self, player):
        # Horizontales
        if self.board[0] == player and self.board[1] == player and self.board[2] == player:
            return True
        elif self.board[3] == player and self.board[4] == player and self.board[5] == player:
            return True
        elif self.board[6] == player and self.board[7] == player and self.board[8] == player:
            return True

        #verticales
        if self.board[0] == player and self.board[3] == player and self.board[6] == player:
            return True
        elif self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        elif self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True

        #Diagonales
        if self.board[0] == player and self.board[4] == player and self.board[8] == player:
            return True
        elif self.board[2] == player and self.board[4] == player and self.board[6] == player:
            return True

    def InvertBoard(self, board):
        inverted = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        i = 0
        for value in board:
            if value == 1:
                inverted[i] = -1
            elif value == -1:
                inverted[i] = 1

            i += 1

        return inverted

    def Copy(self):
        copied = []

        for i in self.board:
            copied.append(i)

        return copied

    def Print(self):
        TextBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

        i = 0
        for value in self.board:
            if value == 1:
                TextBoard[i] = "X"
            elif value == -1:
                TextBoard[i] = "O"

            i += 1

        print ""
        print TextBoard[0], TextBoard[1], TextBoard[2]
        print TextBoard[3], TextBoard[4], TextBoard[5]
        print TextBoard[6], TextBoard[7], TextBoard[8]

    def IsEmpty(self, index):
        return self.board[index - 1] == 0
