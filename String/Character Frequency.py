def freqCount(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq 
 
print(freqCount("hello world"))