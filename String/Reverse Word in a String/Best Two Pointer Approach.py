class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = n - 1
        result = []

        while i >= 0:
            # skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:
                break

            j = i
            # capture word
            while i >= 0 and s[i] != " ":
                i -= 1

            result.append(s[i + 1 : j + 1])

        return " ".join(result)


# ⏱️ Complexity

# Time: O(n)

# Space: O(n) (result list)