from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            if len(ans) <= p[1]:
                ans.append(p)
            elif len(ans) > p[1]:
                ans.insert(p[1], p)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))