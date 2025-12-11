def countVowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)
print(countVowels("eeeee"))