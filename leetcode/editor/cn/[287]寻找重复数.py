from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num in hashset:
                return num
            else:
                hashset.add(num)

# leetcode submit region end(Prohibit modification and deletion)
