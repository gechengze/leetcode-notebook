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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        ans = 0
        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans = curr_sum

        return ans
# leetcode submit region end(Prohibit modification and deletion)
