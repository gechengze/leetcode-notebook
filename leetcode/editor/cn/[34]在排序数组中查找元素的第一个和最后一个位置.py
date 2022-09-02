from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def left_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target <= nums[mid]:
                    right = mid - 1
                if target > nums[mid]:
                    left = mid + 1
            return left

        a = left_search(nums, target)
        b = left_search(nums, target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]

# leetcode submit region end(Prohibit modification and deletion)
