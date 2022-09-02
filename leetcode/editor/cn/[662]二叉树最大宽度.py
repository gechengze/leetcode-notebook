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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        arr = [[root, 1]]
        while arr:
            tmp = []
            for node, index in arr:
                if node.left:
                    tmp.append([node.left, index * 2])
                if node.right:
                    tmp.append([node.right, index * 2 + 1])
            ans = max(ans, arr[-1][1] - arr[0][1] + 1)
            arr = tmp
        return ans


# leetcode submit region end(Prohibit modification and deletion)


root = list2tree([1,3,2,5,3,None,9,])
print(Solution().widthOfBinaryTree(root))

root = list2tree([1,3,2,5,None,None,9,6,None,None,None,None,None,7])
print(Solution().widthOfBinaryTree(root))

root = list2tree([1,3,2,5])
print(Solution().widthOfBinaryTree(root))

root = list2tree([0,0,0,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None])
print(Solution().widthOfBinaryTree(root))

