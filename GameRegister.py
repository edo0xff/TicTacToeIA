class Register:

    def __init__(self):
        self.game = []

    def SaveMovement(self, movement):
        if not movement in self.game:
            self.game.append(movement)

    def GetGame(self):
        return self.game

    def Len(self):
        return len(self.game)
