import re

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveEquation(self, equation: str) -> str:
        left = equation.split('=')[0]
        if left.startswith('-'):
            left = '0' + left
        left_num = re.split('\+|\-', left)
        left_sym = ['+'] + re.findall('\+|\-', left)
        l1 = 0
        l2 = 0
        for i in range(len(left_num)):
            if 'x' in left_num[i]:
                if left_sym[i] == '+':
                    if len(left_num[i]) > 1:
                        l1 += int(left_num[i].replace('x', ''))
                    else:
                        l1 += 1
                else:
                    if len(left_num[i]) > 1:
                        l1 -= int(left_num[i].replace('x', ''))
                    else:
                        l1 -= 1
            else:
                if left_sym[i] == '+':
                    l2 += int(left_num[i])
                else:
                    l2 -= int(left_num[i])

        right = equation.split('=')[1]
        if right.startswith('-'):
            right = '0' + right
        right_num = re.split('\+|\-', right)
        right_sym = ['+'] + re.findall('\+|\-', right)
        r1 = 0
        r2 = 0
        for i in range(len(right_num)):
            if 'x' in right_num[i]:
                if right_sym[i] == '+':
                    if len(right_num[i]) > 1:
                        r1 += int(right_num[i].replace('x', ''))
                    else:
                        r1 += 1
                else:
                    if len(right_num[i]) > 1:
                        r1 -= int(right_num[i].replace('x', ''))
                    else:
                        r1 -= 1
            else:
                if right_sym[i] == '+':
                    r2 += int(right_num[i])
                else:
                    r2 -= int(right_num[i])

        n_x = l1 - r1
        n_n = r2 - l2
        # print(n_x, n_n)
        if n_x == 0:
            if n_n == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x=' + str(n_n // n_x)

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().solveEquation("-x=-1"))
print(Solution().solveEquation("x+5-3+4+x=6+x-2"))
print(Solution().solveEquation("2x=x"))
print(Solution().solveEquation("2x=4x"))
print(Solution().solveEquation("x=x"))
print(Solution().solveEquation("x+2=x+3"))


