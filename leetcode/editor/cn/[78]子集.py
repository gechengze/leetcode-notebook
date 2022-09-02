from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(path, start):
            ans.append(path[:])
            if len(path) == len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        dfs([], 0)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().subsets([0]))