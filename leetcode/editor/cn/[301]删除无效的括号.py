from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        lremove, rremove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def is_valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def dfs(s, start, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if is_valid(s):
                    ans.append(s)
                return
            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                if lremove + rremove > len(s) - i:
                    break
                if lremove > 0 and s[i] == '(':
                    dfs(s[:i] + s[i + 1:], i, lremove - 1, rremove)
                if rremove > 0 and s[i] == ')':
                    dfs(s[:i] + s[i + 1:], i, lremove, rremove - 1)

        dfs(s, 0, lremove, rremove)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
