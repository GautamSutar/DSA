class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []

        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            result.append(s % 10)
            carry = s // 10

        if carry:
            result.append(carry)

        return result[::-1]



# Time Complexity
# O(n)

# Space Complexity
# O(n)

# ✔️ Safe
# ✔️ Clear logic
# ❌ Uses extra array