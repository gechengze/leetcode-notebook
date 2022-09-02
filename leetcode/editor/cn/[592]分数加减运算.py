import re


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, a: str, b: str, plus_or_minus):
        fenmu = int(a.split('/')[1]) * int(b.split('/')[1])
        if plus_or_minus == '+':
            fenzi = int(a.split('/')[0]) * int(b.split('/')[1]) + int(b.split('/')[0]) * int(a.split('/')[1])
        else:
            fenzi = int(a.split('/')[0]) * int(b.split('/')[1]) - int(b.split('/')[0]) * int(a.split('/')[1])
        x, y = fenzi, fenmu
        while fenmu > 0:
            fenzi, fenmu = fenmu, fenzi % fenmu
        x = int(x / fenzi)
        y = int(y / fenzi)

        return str(x) + '/' + str(y)

    def fractionAddition(self, expression: str) -> str:
        expression_split = re.split('\+|\-', expression)
        if expression_split[0] == '':
            expression_split[0] = '0/1'
        is_positive = re.findall('\+|\-', expression)

        for i in range(len(expression_split) - 1):
            expression_split[i + 1] = self.calculate(expression_split[i], expression_split[i + 1], is_positive[i])
        # print(expression_split)
        return expression_split[-1]

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().fractionAddition("-1/2+1/2+1/3-1/4-1/6+1/5"))
print(Solution().fractionAddition("1/2+1/2+1/3-1/4-1/6+1/5"))