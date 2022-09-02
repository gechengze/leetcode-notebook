from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            grid[i][j] = '0'
            if i + 1 < m and grid[i + 1][j] == '1':
                dfs(i + 1, j)
            if j + 1 < n and grid[i][j + 1] == '1':
                dfs(i, j + 1)
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                dfs(i - 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                dfs(i, j - 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))