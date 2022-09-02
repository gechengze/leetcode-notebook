from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rightmax = 0
        for i in range(n):
            if i <= rightmax:
                rightmax = max(rightmax, i + nums[i])
                if rightmax >= n - 1:
                    return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
