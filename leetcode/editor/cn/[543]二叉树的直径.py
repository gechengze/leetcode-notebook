from typing import Optional
from playground import TreeNode, list2tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            self.ans = max(self.ans, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)


root = list2tree([1,2,3,4,5])
print(Solution().diameterOfBinaryTree(root))

root = list2tree([1])
print(Solution().diameterOfBinaryTree(root))

root = list2tree([1,2,3])
print(Solution().diameterOfBinaryTree(root))

root = list2tree([2,3,None,1])
print(Solution().diameterOfBinaryTree(root))