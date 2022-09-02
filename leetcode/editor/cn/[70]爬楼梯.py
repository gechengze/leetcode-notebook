# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1, 1]
        for _ in range(n - 1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().climbStairs(45))