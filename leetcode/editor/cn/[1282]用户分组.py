import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashtable = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            hashtable[size].append(i)
        ans = []
        for k, v in hashtable.items():
            for i in range(0, len(v), k):
                ans.append(v[i: i + k])

        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().groupThePeople([3,3,3,3,3,1,3]))
print(Solution().groupThePeople([2,1,3,3,3,2]))
