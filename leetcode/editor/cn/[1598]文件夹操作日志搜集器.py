from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "./":
                continue
            if log != "../":
                depth += 1
            elif depth:
                depth -= 1
        return depth

# leetcode submit region end(Prohibit modification and deletion)
