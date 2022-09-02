from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            l2r[i + 1] = l2r[i] * nums[i]

        r2l = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, 0, -1):
            r2l[i - 1] = r2l[i] * nums[i]

        ans = []
        for i in range(len(nums)):
            ans.append(l2r[i] * r2l[i])
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().productExceptSelf([1,2,3,4,5]))