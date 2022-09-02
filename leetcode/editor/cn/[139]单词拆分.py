from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        memo = [None] * n

        def dfs(start):
            if start == n:
                return True
            if memo[start] is not None:
                return memo[start]
            for i in range(start + 1, n + 1):
                if s[start: i] in wordDict and dfs(i):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dfs(0)

# leetcode submit region end(Prohibit modification and deletion)
