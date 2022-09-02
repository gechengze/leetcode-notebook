from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, ans = 1e5, 0
        for price in prices:
            ans = max(price - min_price, ans)
            min_price = min(price, min_price)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
