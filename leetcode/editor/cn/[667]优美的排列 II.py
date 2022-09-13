from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            answer.append(i)
            if i != j:
                answer.append(j)
            i, j = i + 1, j - 1
        return answer

# leetcode submit region end(Prohibit modification and deletion)
