# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().hammingDistance(1, 4))
print(Solution().hammingDistance(3, 1))