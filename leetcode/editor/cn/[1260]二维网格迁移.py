from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        temp = []
        for row in grid:
            temp.extend(row)
        k = k % len(temp)
        temp = temp[-k:] + temp[:len(temp) - k]
        for i in range(m):
            grid[i] = temp[i * n: i * n + n]
        return grid


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().shiftGrid([[1],[2],[3],[4],[7],[6],[5]], k=23))
print(Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k=1))
print(Solution().shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k=4))