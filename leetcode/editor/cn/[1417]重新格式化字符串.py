# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformat(self, s: str) -> str:
        alpha, num = [], []
        for c in s:
            if 'a' <= c <= 'z':
                alpha.append(c)
            else:
                num.append(c)

        ans = ''
        if len(alpha) == len(num):
            for i in range(len(alpha)):
                ans += alpha[i]
                ans += num[i]
        elif len(alpha) - len(num) == 1:
            for i in range(len(num)):
                ans += alpha[i]
                ans += num[i]
            ans += alpha[-1]
        elif len(num) - len(alpha) == 1:
            for i in range(len(alpha)):
                ans += num[i]
                ans += alpha[i]
            ans += num[-1]

        return ans

# leetcode submit region end(Prohibit modification and deletion)
