import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v: abs(v - x))
        return sorted(arr[:k])


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1))
