# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.s = ''
        self.n = 0

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.n = len(s)
        left, right = 0, 0
        for i in range(self.n):
            l, r = self.expand(i, i)
            if r - l > right - left:
                left, right = l, r
            if i < self.n - 1 and s[i] == s[i + 1]:
                l, r = self.expand(i, i + 1)
                if r - l > right - left:
                    left, right = l, r

        return s[left: right + 1]

    def expand(self, left, right):
        while left > 0 and right < self.n - 1 and self.s[left - 1] == self.s[right + 1]:
            left -= 1
            right += 1
        return left, right

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().longestPalindrome(s="babad"))