from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j , start):
            if start == len(word) - 1:
                return board[i][j] == word[start]
            if board[i][j] == word[start]:
                temp = board[i][j]
                board[i][j] = 0
                for k in range(4):
                    next_x, next_y = i + directions[k][0], j + directions[k][1]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        if dfs(next_x, next_y, start + 1):
                            return True
                board[i][j] = temp

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

# leetcode submit region end(Prohibit modification and deletion)
