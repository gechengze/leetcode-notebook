from typing import Optional, List
from playground import TreeNode, list2tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        queue = [root]
        n_row = 0
        while queue:
            n_row += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        n_col = 2 ** n_row - 1
        ans = [[None] * n_col for _ in range(n_row)]
        ans[0][(n_col - 1) // 2] = root

        for r in range(n_row - 1):
            for c in range(n_col):
                node = ans[r][c]
                if node and node.left:
                    ans[r + 1][c - 2 ** (n_row - r - 2)] = node.left
                if node and node.right:
                    ans[r + 1][c + 2 ** (n_row - r - 2)] = node.right

        for r in range(n_row):
            for c in range(n_col):
                if ans[r][c]:
                    ans[r][c] = str(ans[r][c].val)
                else:
                    ans[r][c] = ''
        return ans


# leetcode submit region end(Prohibit modification and deletion)


root = list2tree([1, 2, 3, None, 4])
print(Solution().printTree(root))
