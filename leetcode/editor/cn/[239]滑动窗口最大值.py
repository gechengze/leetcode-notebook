from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = []
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]])

        for i in range(k, len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            while queue[0] <= i - k:
                queue.pop(0)
            ans.append(nums[queue[0]])

        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], k=3))