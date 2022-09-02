from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        for word in sentence.split(' '):
            min_len = len(word)
            temp = word
            for root in dictionary:
                if len(root) <= min_len and word[0: len(root)] == root:
                    temp = root
                    min_len = len(temp)
            ans.append(temp)

        return ' '.join(ans)

# leetcode submit region end(Prohibit modification and deletion)


# print(Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
# print(Solution().replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
print(Solution().replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
