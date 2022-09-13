# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        left, right = 0, 0
        for i in range(n - 1):
            cur_max = num[i]
            flag = False
            for j in range(i + 1, n):
                if num[j] > num[i] and num[j] >= cur_max:
                    cur_max = num[j]
                    left = i
                    right = j
                    flag = True
            if flag:
                break
        num[left], num[right] = num[right], num[left]
        return int(''.join(num))

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().maximumSwap(1993))
print(Solution().maximumSwap(2736))
print(Solution().maximumSwap(9973))
print(Solution().maximumSwap(98368))