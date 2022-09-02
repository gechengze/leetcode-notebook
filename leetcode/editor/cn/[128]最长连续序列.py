from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                curr_num = num
                temp = 1
                while curr_num + 1 in nums:
                    curr_num += 1
                    temp += 1
                ans = max(ans, temp)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
