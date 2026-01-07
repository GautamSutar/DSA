class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set("aeiou")
        ans = 0

        for i in range(n):
            vowel_count = {v: 0 for v in vowels}
            consonants = 0

            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    vowel_count[ch] += 1
                else:
                    consonants += 1

                if consonants > k:
                    break

                if consonants == k and all(vowel_count[v] > 0 for v in vowels):
                    ans += 1

        return ans
# ⏱ Complexity

# Time: O(n²) ❌

# Space: O(1)

# ➡️ Still too slow for large inputs