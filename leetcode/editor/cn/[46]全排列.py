from typing import List
from itertools import permutations


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(path: List, used: List):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path, used)
                path.pop()
                used[i] = False

        dfs([], [False] * n)

        return ans

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().permute([1,2,3]))