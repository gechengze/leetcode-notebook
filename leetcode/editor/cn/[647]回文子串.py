# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        def expand(l, r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt

        for i in range(n):
            ans += expand(i, i)
            if i < n - 1 and s[i] == s[i + 1]:
                ans += expand(i, i + 1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().countSubstrings('abc'))