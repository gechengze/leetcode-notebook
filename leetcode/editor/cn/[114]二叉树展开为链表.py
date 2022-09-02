from playground import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        nodelist = []

        def dfs(root):
            if not root:
                return
            nodelist.append(root)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        for i in range(len(nodelist) - 1):
            nodelist[i].left = None
            nodelist[i].right = nodelist[i + 1]
        nodelist[-1].left = None
        nodelist[-1].right = None

# leetcode submit region end(Prohibit modification and deletion)
