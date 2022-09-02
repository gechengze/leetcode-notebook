from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        l, r = -1, -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                l = i
                break
        for i in range(len(nums) - 1, l, -1):
            if nums[i] != sorted_nums[i]:
                r = i
                break
        if l == -1 and r == -1:
            return 0
        return r - l + 1


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(Solution().findUnsortedSubarray([1, 2, 3, 4]))
print(Solution().findUnsortedSubarray([1,2,3,4,6,1,5,7,83,6]))


