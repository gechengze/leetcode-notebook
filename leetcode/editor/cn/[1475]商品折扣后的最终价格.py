from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().finalPrices([8,4,6,2,3]))
print(Solution().finalPrices([1,2,3,4,5]))

