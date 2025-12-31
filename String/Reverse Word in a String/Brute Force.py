class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []
        word = ""
        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word != "":
                    word_list.append(word)
                    word = ""

        if word != "":
            word_list.append(word)

        result = ""
        for i in range(len(word_list) - 1, -1, -1):
            result += word_list[i]
            if i != 0:
                result += " "
        return result


# Complexity
# Time: O(n)
# Space: O(n) (words list)