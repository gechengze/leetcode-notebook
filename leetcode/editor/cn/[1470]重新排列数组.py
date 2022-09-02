from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for x, y in zip(nums[:n], nums[n:]):
            ans.append(x)
            ans.append(y)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().shuffle([2,5,1,3,4,7], 3))