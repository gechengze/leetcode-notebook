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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        curr_sum = 0

        def dfs(root):
            nonlocal curr_sum
            if root.right:
                dfs(root.right)
            root.val += curr_sum
            curr_sum = root.val
            if root.left:
                dfs(root.left)

        dfs(root)

        return root
# leetcode submit region end(Prohibit modification and deletion)


root = list2tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
print(Solution().convertBST(root))