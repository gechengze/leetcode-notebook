from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(n // 2):
            for i in range(j, n - 1 - j):
                matrix[j][i], matrix[i][n - 1 - j], matrix[n - 1 - j][n - 1 - i], matrix[n - 1 - i][j] = \
                    matrix[n - 1 - i][j], matrix[j][i], matrix[i][n - 1 - j], matrix[n - 1 - j][n - 1 - i]

        # for i in matrix:
        #     print(i)
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))