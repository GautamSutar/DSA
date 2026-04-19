class NonRepeatingCharacter:
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
            if result[ch] == 1:        
                return ch
            else:
                return "$"

string = "aabbccc"
obj = NonRepeatingCharacter(string)
print(obj.printFreq())