from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 10 ** 7
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        ans = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                ans.append([arr[i - 1], arr[i]])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
