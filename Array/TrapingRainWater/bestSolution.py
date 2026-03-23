class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        leftMax = 0
        rightMax = 0

        left = 0
        right = n - 1

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1
        return water


# Time = O(n)
# Space = O(1)
