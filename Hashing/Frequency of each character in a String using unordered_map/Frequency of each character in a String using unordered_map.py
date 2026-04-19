class ToCheckSubset:
    def __init__(self, s):
        self.s = s
        self.freq = {}
    def check(self):
        for num in self.s:
            self.freq[num] = self.freq.get(num, 0) + 1
        return self.freq
    
    def printFreq(self):
        result = self.check()
        for ch in result:
            print(f"{ch} : {result[num]}")

string = "geeksforgeeks"
obj = ToCheckSubset(string)
print(obj.printFreq())