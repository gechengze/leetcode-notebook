from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])
        return 1 - min(prefix_sum) if min(prefix_sum) < 0 else 1
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().minStartValue([-3,2,-3,4,2]))