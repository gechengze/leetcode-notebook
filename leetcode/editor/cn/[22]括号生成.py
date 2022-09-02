from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(path, n_left, n_right):
            if len(path) == 2 * n:
                ans.append(path)
                return
            if n_left < n:
                path += '('
                dfs(path, n_left + 1, n_right)
                path = path[:-1]
            if n_right < n_left:
                path += ')'
                dfs(path, n_left, n_right + 1)

        ans = []
        dfs('', 0, 0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().generateParenthesis(3))