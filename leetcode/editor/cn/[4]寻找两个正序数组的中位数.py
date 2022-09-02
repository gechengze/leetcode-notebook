from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        return nums1[n // 2] / 1 if n % 2 != 0 else (nums1[n // 2 - 1] + nums1[n // 2]) / 2
# leetcode submit region end(Prohibit modification and deletion)
