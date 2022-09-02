from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        left = 0
        while left < n:

            while left < n and nums[left] != 0:
                left += 1
            right = left + 1
            while right < n and nums[right] == 0:
                right += 1
            if right < n:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
        print(nums)
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().moveZeroes([1, 0, 1]))
print(Solution().moveZeroes([1, 0]))
print(Solution().moveZeroes([0,0,1]))
print(Solution().moveZeroes([0,1,0,3,12]))
print(Solution().moveZeroes([0]))
