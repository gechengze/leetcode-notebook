from typing import List
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        for curr, prev in prerequisites:
            edges[prev].append(curr)

        visited = [0] * numCourses
        valid = True

        def dfs(i):
            nonlocal valid
            visited[i] = True
            for v in edges[i]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[i] = 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        return valid
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().canFinish(2, [[0,1]]))
print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(2, [[1,0], [0,1]]))
print(Solution().canFinish(7, [[1,0], [0,2], [2,4],[4,6],[6,0]]))
