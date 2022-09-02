from typing import Optional
from playground import TreeNode, list2link


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            arr.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)
        print(arr)

        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
