from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        for row, col in indices:
            for i in range(m):
                matrix[i][col] += 1
            for i in range(n):
                matrix[row][i] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    ans += 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().oddCells(2,2,[[1,1],[0,0]]))