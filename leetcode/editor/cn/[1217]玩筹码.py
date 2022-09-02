from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for p in position:
            if p % 2 != 0:
                odd += 1
            else:
                even += 1
        return min(odd, even)
# leetcode submit region end(Prohibit modification and deletion)
