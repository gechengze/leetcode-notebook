from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = dict()
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        ans = 0
        for num, cnt in hashtable.items():
            if cnt > len(nums) // 2:
                ans = num
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().majorityElement([3,2,3]))