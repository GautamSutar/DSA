class Nqueen:
    def __init__(self, n):
        self.n = n
        self.board = [["." for _ in range(n)] for _ in range(n)]
        self.solution = []

    def solve(self):
        self.backtrack(0)
        return self.solution

    def backtrack(self, row):
        if row == self.n:
            self.saveSolution()
            return

        for col in range(self.n):
            if self.isSafe(row, col):
                self.board[row][col] = "Q"
                self.backtrack(row + 1)
                self.board[row][col] = "."

    def isSafe(self, row, col):
        for i in range(row):
            if self.board[i][col] == "Q":
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def saveSolution(self):
        result = ["".join(row) for row in self.board]
        return self.solution.append(result)

    def printBoard(self):
        for row in self.board:
            print("".join(row))
        print()


obj = Nqueen(4)
result = obj.solve()
for sol in result:
    for row in sol:
        print(row)
    print()
