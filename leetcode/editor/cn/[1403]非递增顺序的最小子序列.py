from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        n = sum(nums) // 2
        temp = 0
        ans = []
        for num in nums:
            temp += num
            ans.append(num)
            if temp > n:
                break
        return ans
# leetcode submit region end(Prohibit modification and deletion)
