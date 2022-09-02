import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = collections.defaultdict(list)
        for word in strs:
            hashtable[tuple(sorted(list(word)))].append(word)
        return list(hashtable.values())


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))