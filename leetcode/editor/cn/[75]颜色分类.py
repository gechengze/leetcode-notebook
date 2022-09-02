from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        i, zero, two = 0, 0, len(nums)
        while i < two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]



# leetcode submit region end(Prohibit modification and deletion)


print(Solution().sortColors([2,0,2,1,1,0]))