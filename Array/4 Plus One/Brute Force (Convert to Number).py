class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num * 10 + d

        num += 1

        result = []
        while num > 0:
            result.append(num % 10)
            num //= 10

        return result[::-1]


# Time Complexity
# O(n)

# Space Complexity
# O(n)

# ❌ Risky in languages with integer overflow
# ❌ Interviewers usually reject this