import math
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ''

        hashtable = collections.defaultdict(int)
        for c in t:
            hashtable[c] += 1

        start, end, min_start, min_len, count = 0, 0, 0, math.inf, len(t)
        while end < len(s):
            if hashtable[s[end]] > 0:
                count -= 1
            hashtable[s[end]] -= 1
            end += 1
            while count == 0:
                if end - start < min_len:
                    min_start = start
                    min_len = end - start
                hashtable[s[start]] += 1
                if hashtable[s[start]] > 0:
                    count += 1
                start += 1

        return '' if min_len == math.inf else s[min_start: min_start + min_len]


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow('ab', 'a'))
print(Solution().minWindow('a', 'a'))
print(Solution().minWindow('a', 'aa'))