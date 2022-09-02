from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            flag = True
            while flag and stack and stack[-1] > 0 > asteroid:
                a, b = stack[-1], -asteroid
                if a <= b:
                    stack.pop(-1)
                if a >= b:
                    flag = False
            if flag:
                stack.append(asteroid)
        return stack

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().asteroidCollision([5, 10, -5]))