class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(n):
            leftMax = max(height[: i + 1])
            rightMax = max(height[i:])
            water += min(leftMax, rightMax) - height[i]
        return water


# Time = O(n ^ 2)
# Space = O(1)
