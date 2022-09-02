from typing import List
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        return (-heapq.heappop(heap) - 1) * (-heapq.heappop(heap) - 1)
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().maxProduct([3,4,5,2]))
print(Solution().maxProduct([1,5,4,5]))
print(Solution().maxProduct([3,7]))