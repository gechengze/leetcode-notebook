import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]
        edge_square = []
        for i in range(3):
            for j in range(i + 1, 4):
                if i != j:
                    edge_square.append((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2)
        edge_count = dict(collections.Counter(edge_square))

        if not len(edge_count) == 2 or any([x == 0 for x in edge_count.keys()]) or not (sorted(edge_count.values())[0] == 2 and sorted(edge_count.values())[1] == 4):
            return False

        return True

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().validSquare([0,0], [1,1], [0,0], [1,1]))
print(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
print(Solution().validSquare([0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))
print(Solution().validSquare([2,0], p2 = [2,4], p3 = [1,2], p4 = [3,2]))

