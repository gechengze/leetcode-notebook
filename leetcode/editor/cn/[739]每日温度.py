from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                temp = stack.pop()
                ans[temp] = i - temp
            stack.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))