# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if c == ')' and temp != '(':
                    return False
                if c == ']' and temp != '[':
                    return False
                if c == '}' and temp != '{':
                    return False
        return len(stack) == 0
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().isValid(']'))