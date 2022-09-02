import heapq
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        cnt = [(-v, k) for k, v in cnt.items()]
        heap = []
        for n in cnt:
            heapq.heappush(heap, n)

        ans = [heapq.heappop(heap)[1] for _ in range(k)]

        return ans

    # leetcode submit region end(Prohibit modification and deletion)


# print(Solution().topKFrequent([1,2], 2))
print(Solution().topKFrequent([1,1,1,2,2,3,3,3,3], 2))