class Nqueen:
    def __init__(self, n):
        self.n = n
        self.board = [["." for _ in range(n)] for _ in range(n)]
        self.solution = []

    def printBoard(self):
        for row in self.board:
            print("".join(row))
        print()


class CallingMethod:
    def calling(self, num, obj):
        if num == 1:
            return obj.printBoard()


obj = Nqueen(4)
choice = int(input("What do you want to print? { Press 1 for Printing Board }: "))
obj1 = CallingMethod()
obj1.calling(choice, obj)
