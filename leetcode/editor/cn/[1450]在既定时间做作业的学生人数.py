from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
