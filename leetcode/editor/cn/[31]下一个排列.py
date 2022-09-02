from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        i, j, k = n - 2, n - 1, n - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        nums[j:] = nums[j:][::-1]
        print(nums)
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().nextPermutation([1,1]))
print(Solution().nextPermutation([1,5,1]))
print(Solution().nextPermutation([5,1,1]))