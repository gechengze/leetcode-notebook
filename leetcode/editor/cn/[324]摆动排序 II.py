from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        arr = sorted(nums)
        x = (n + 1) // 2
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1

        """
        Do not return anything, modify nums in-place instead.
        """
# leetcode submit region end(Prohibit modification and deletion)

print(Solution().wiggleSort([0,1,2,3,4,5]))