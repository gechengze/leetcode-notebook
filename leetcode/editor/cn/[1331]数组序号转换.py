from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        hashtable = {}
        i = 1
        for num in sorted_arr:
            if num not in hashtable:
                hashtable[num] = i
                i += 1
        return [hashtable[num] for num in arr]

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().arrayRankTransform([40,10,20,30]))
print(Solution().arrayRankTransform([10,10,10]))
print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))