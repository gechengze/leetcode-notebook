from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr = []
        for interval in intervals:
            arr.append((interval[0], 'start'))
            arr.append((interval[1], 'end'))
        arr.sort()

        ans, temp = 0, 0
        for _, start_or_end in arr:
            if start_or_end == 'start':
                temp += 1
            else:
                temp -= 1
            ans = max(ans, temp)

        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().minMeetingRooms([[0,30],[5,10],[15,20]]))
print(Solution().minMeetingRooms([[7,10],[2,4]]))