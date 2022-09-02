# leetcode submit region begin(Prohibit modification and deletion)
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(p)
        result = re.match(pattern, s)
        if not result:
            return False
        return result[0] == s
# leetcode submit region end(Prohibit modification and deletion)


# print(Solution().isMatch('aa', 'a'))
# print(Solution().isMatch('aa', 'a*'))
print(Solution().isMatch('ab', '.*c'))