def isAnagrams(s, t):
    return sorted(s) == sorted(t)

print(isAnagrams("listen", "silent"))