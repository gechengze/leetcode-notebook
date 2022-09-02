import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        def isPrime(n: int) -> int:
            if n == 1:
                return 0
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return 0
            return 1

        def factorial(n: int) -> int:
            res = 1
            for i in range(1, n + 1):
                res *= i
                res %= (10 ** 9 + 7)
            return res

        numPrimes = sum(isPrime(i) for i in range(1, n + 1))
        return factorial(numPrimes) * factorial(n - numPrimes) % (10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)
