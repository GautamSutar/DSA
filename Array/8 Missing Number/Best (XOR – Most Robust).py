class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


# | Approach | Time       | Space    | Notes     |
# | -------- | ---------- | -------- | --------  |
# | Brute    | O(n²)      | O(1)     | ❌        |
# | Sort     | O(n log n) | O(1)     | ❌        |
# | Sum      | **O(n)**   | **O(1)** | ✅        |
# | XOR      | **O(n)**   | **O(1)** | ✅ safest |
