from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        alphabet = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def dfs(path, index):
            if index == n:
                ans.append(path)
                return
            for c in alphabet[int(digits[index])]:
                path += c
                dfs(path, index + 1)
                path = path[:-1]

        ans = []
        dfs('', 0)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().letterCombinations('234234'))