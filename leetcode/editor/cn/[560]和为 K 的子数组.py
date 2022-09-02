from typing import List
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 要求的连续子数组
        count = 0
        n = len(nums)
        preSums = collections.defaultdict(int)
        preSums[0] = 1

        presum = 0
        for i in range(n):
            presum += nums[i]

            # if preSums[presum - k] != 0:
            count += preSums[presum - k]  # 利用defaultdict的特性，当presum-k不存在时，返回的是0。这样避免了判断

            preSums[presum] += 1  # 给前缀和为presum的个数加1

        return count

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().subarraySum([1,-1,0],0))
print(Solution().subarraySum([-3,-2,-1,1,2,3,4],3))
print(Solution().subarraySum([1],0))
print(Solution().subarraySum([1,1,1],2))
print(Solution().subarraySum([1,2,3],3))