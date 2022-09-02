from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left2right = [0] * n
        right2left = [0] * n

        left2right[0] = height[0]
        for i in range(1, n):
            left2right[i] = max(height[i], left2right[i - 1])

        right2left[-1] = height[-1]
        for i in range(n - 2, - 1, -1):
            right2left[i] = max(height[i], right2left[i + 1])

        ans = 0
        for i in range(1, n - 1):
            ans += min(left2right[i], right2left[i]) - height[i]

        return ans


# leetcode submit region end(Prohibit modification and deletion)
