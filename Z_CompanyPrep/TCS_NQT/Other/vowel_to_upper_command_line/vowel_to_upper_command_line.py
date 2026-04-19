import sys


if len(sys.argv) != 2:
    sys.exit()

s = sys.argv[1]

vowel = "aeiouAEIOU"
result = ""
for ch in s:
    if ch in vowel:
        result += ch.upper()
    else:
        result += ch

print(result)
