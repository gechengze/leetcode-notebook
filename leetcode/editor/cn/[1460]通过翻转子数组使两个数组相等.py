import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().canBeEqual([1,2,2,3],[1,1,2,3]))