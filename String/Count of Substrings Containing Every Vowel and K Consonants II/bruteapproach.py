class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set("aeiou")
        ans = 0

        for i in range(n):
            for j in range(i, n):
                vowel_set = set()
                consonants = 0

                for ch in word[i : j + 1]:
                    if ch in vowels:
                        vowel_set.add(ch)
                    else:
                        consonants += 1

                if len(vowel_set) == 5 and consonants == k:
                    ans += 1

        return ans


# ⏱ Complexity

# Time: O(n³) ❌

# Space: O(1)

# ➡️ Will TLE for n = 2×10⁵