from typing import List
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n_words = len(words)
        if n_words == 0:
            return ans

        n_word = len(words[0])
        hashtable1 = dict(collections.Counter(words))

        for i in range(len(s) - n_words * n_word + 1):
            hashtable2 = collections.defaultdict(int)
            j = 0
            while j < n_words:
                temp = s[i + j * n_word: i + (j + 1) * n_word]
                if temp in hashtable1:
                    hashtable2[temp] += 1
                    if hashtable2[temp] > hashtable1[temp]:
                        break
                else:
                    break
                j += 1

            if j == n_words:
                ans.append(i)

        return ans
# leetcode submit region end(Prohibit modification and deletion)

print(Solution().findSubstring(s="barfoothefoobarman", words=["foo","bar"]))