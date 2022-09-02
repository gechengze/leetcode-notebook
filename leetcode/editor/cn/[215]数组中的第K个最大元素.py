import random
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left


def topk_split(nums, k, left, right):
    if left < right:
        index = partition(nums, left, right)
        if index == k:
            return
        elif index < k:
            topk_split(nums, k, index + 1, right)
        else:
            topk_split(nums, k, left, index - 1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        topk_split(nums, len(nums) - k, 0, len(nums) - 1)
        return nums[len(nums) - k]

# leetcode submit region end(Prohibit modification and deletion)
