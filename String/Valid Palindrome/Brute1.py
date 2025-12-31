# import re

# text = "race a car"
# clean_text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
# original_word = ""
# for ch in clean_text:
#     if ch != " ":
#         original_word += ch.lower()

# print(original_word)
# rev = ""
# for i in range(len(original_word) - 1, -1, -1):
#     rev += original_word[i]
# if rev == original_word:
#     print("Palindrome")


import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r"[^a-zA-Z0-9 ]", "", s)
        original_word = ""
        for ch in clean_text:
            if ch != " ":
                original_word += ch.lower()
        rev = ""
        for i in range(len(original_word) - 1, -1, -1):
            rev += original_word[i]
        if rev == original_word:
            return True
        else:
            return False

# Complexity
# Time: O(n)
# Space: O(n) (words list)
