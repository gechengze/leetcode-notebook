from typing import List
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        ans = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i: i + len(p)]) == cnt:
                ans.append(i)

        return ans

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().findAnagrams('cbaebabacd', 'abc'))