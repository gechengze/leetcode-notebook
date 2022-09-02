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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            ans = TreeNode(val=val, left=root, right=None)
            return ans

        queue = [root]
        curr_depth = 1
        while queue:
            curr_depth += 1
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curr_depth == depth:
                for node in level:
                    left_temp = node.left
                    right_temp = node.right
                    node.left = TreeNode(val=val, left=left_temp, right=None)
                    node.right = TreeNode(val=val, left=None, right=right_temp)

        return root
# leetcode submit region end(Prohibit modification and deletion)
