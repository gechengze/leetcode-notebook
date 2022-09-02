from typing import List
from itertools import permutations


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}  # 记忆化单元

        # @functools.cache  # Python functools自带记忆化单元【启用后可省去自定义cache单元】
        def dfs(i, summ, t):
            '''summ: 前i个元素的表达式之和; t: 目标值'''
            if (i, summ) in cache:  # 记忆化：已存在，直接返回
                return cache[(i, summ)]

            if i == len(nums):  # 遍历完了全部的元素，递归中止
                if summ == t:  # 找到了一个满足要求的组合
                    cache[(i, summ)] = 1
                else:
                    cache[(i, summ)] = 0
                return cache[(i, summ)]

            pos_cnt = dfs(i + 1, summ + nums[i], t)  # nums[i]前面添加'+'号
            neg_cnt = dfs(i + 1, summ - nums[i], t)  # nums[i]前面添加'-'号
            cache[(i, summ)] = pos_cnt + neg_cnt  # 以上两种情况的组合数之和
            return cache[(i, summ)]

        return dfs(0, 0, target)


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().findTargetSumWays([1,1,1,1,1], 3))