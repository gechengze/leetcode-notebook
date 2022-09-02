# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, val, step=0):
        self.val = val
        self.step = step


class Solution:
    def numSquares(self, n: int) -> int:
        root = Node(n)
        queue = [root]
        visited = {root.val}
        while queue:
            node = queue.pop(0)
            residuals = [node.val - i * i for i in range(1, int(node.val ** 0.5) + 1)]
            for i in residuals:
                new_node = Node(i, node.step + 1)
                if i == 0:
                    return new_node.step
                elif i not in visited:
                    queue.append(new_node)
                    visited.add(i)

# leetcode submit region end(Prohibit modification and deletion)
