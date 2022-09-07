# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_blank = text.count(' ')
        num_word = 0
        words = []
        for word in text.split(' '):
            if len(word) > 0:
                num_word += 1
                words.append(word)
        if num_word == 1:
            return words[0] + ' ' * num_blank

        n1, n2 = divmod(num_blank, num_word - 1)
        ans = ''
        for i in range(num_word - 1):
            ans += words[i]
            ans += ' ' * n1
        ans += words[-1]
        ans += ' ' * n2
        return ans
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().reorderSpaces('  hello'))
print(Solution().reorderSpaces('  this   is  a sentence '))
print(Solution().reorderSpaces(' practice   makes   perfect'))
print(Solution().reorderSpaces('hello   world'))
print(Solution().reorderSpaces('  walks  udp package   into  bar a'))
print(Solution().reorderSpaces('a'))