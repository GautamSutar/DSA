class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atMost(k):
            vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
            vowel_types = 0
            consonants = 0
            left = 0
            res = 0

            for right in range(len(word)):
                ch = word[right]

                if ch in vowels:
                    if vowels[ch] == 0:
                        vowel_types += 1
                    vowels[ch] += 1
                else:
                    consonants += 1

                while consonants > k:
                    left_char = word[left]
                    if left_char in vowels:
                        vowels[left_char] -= 1
                        if vowels[left_char] == 0:
                            vowel_types -= 1
                    else:
                        consonants -= 1
                    left += 1

                if vowel_types == 5:
                    res += left + 1

            return res

        return atMost(k) - atMost(k - 1)
