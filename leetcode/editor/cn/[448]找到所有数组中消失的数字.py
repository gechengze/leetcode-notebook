from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        ans = []
        for num in range(1, n + 1):
            if num not in nums:
                ans.append(num)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))