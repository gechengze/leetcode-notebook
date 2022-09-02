from typing import Optional
from playground import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    level.append(101)
                    continue
                else:
                    level.append(node.val)

                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            for i in range(len(level) // 2):
                if level[i] != level[len(level) - i - 1]:
                    return False

        return True


# leetcode submit region end(Prohibit modification and deletion)
