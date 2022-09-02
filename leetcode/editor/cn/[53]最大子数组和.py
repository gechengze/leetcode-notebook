from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[i - 1] + nums[i]))

        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))