from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = - 2 ** 31
        max_, min_ = 1, 1
        for num in nums:
            if num < 0:
                max_, min_ = min_, max_
            max_ = max(max_ * num, num)
            min_ = min(min_ * num, num)
            ans = max(ans, max_)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
