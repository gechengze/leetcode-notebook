from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        ans = []
        for i, num in enumerate(nums):
            if target - num in hashtable:
                ans.extend([i, hashtable[target - num]])
                break
            else:
                hashtable[num] = i

        return ans
# leetcode submit region end(Prohibit modification and deletion)
