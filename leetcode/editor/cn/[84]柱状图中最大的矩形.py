from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        ans = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                temp = stack.pop()
                ans = max(ans, (i - stack[-1] - 1) * heights[temp])
            stack.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().largestRectangleArea([2,1,5,6,2,3]))