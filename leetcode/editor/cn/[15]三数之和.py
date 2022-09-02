from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n < 3:
            return ans

        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return ans

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                while i + 1 < left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right < n - 2 and nums[right] == nums[right + 1]:
                    right -= 1
                if left >= right:
                    continue
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))