import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)
        m = 0
        c = 0
        for v in cnt.values():
            if v > m:
                m = v
                c = 1
            elif v == m:
                c += 1
        return max(len(tasks), (n + 1) * (m - 1) + c)
# leetcode submit region end(Prohibit modification and deletion)
