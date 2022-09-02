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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent, cur = None, root
        while cur:
            if val > cur.val:
                if not parent:
                    return TreeNode(val, left=cur, right=None)
                node = TreeNode(val, left=cur, right=None)
                parent.right = node
                return root
            else:
                parent = cur
                cur = cur.right
        parent.right = TreeNode(val)
        return root

# leetcode submit region end(Prohibit modification and deletion)
