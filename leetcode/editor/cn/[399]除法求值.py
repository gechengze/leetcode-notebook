from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.father = {}
        self.value = {}

    def find(self, x):
        root = x
        base = 1
        while self.father[root]:
            root = self.father[root]
            base *= self.value[root]

        while x != root:
            origin_father = self.father[x]
            self.value[x] *= base
            base /= self.value[origin_father]
            self.father[x] = root
            x = origin_father

        return root

    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)
        ans = []
        for a, b in queries:
            if uf.is_connected(a, b):
                ans.append(uf.value[a] / uf.value[b])
            else:
                ans.append(-1.0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))