from typing import List, Optional
from playground import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = [root]

        while queue:
            level_max = -2 ** 31 - 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_max)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
