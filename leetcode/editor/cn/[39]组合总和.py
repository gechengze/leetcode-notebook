from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(combination, start, sum):
            if sum >= target:
                if sum == target:
                    ans.append(combination[:])
                return
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                dfs(combination, i, sum + candidates[i])
                combination.pop()

        dfs([], 0, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
