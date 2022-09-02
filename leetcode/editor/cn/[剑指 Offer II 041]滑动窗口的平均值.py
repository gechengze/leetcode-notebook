import math

# leetcode submit region begin(Prohibit modification and deletion)
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.arr = []

    def next(self, val: int) -> float:
        self.arr.append(val)
        if len(self.arr) <= self.size:
            return sum(self.arr) / len(self.arr)
        else:
            temp = 0
            for i in range(len(self.arr) - 1, len(self.arr) - self.size - 1, -1):
                temp += self.arr[i]
            return temp / self.size




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# leetcode submit region end(Prohibit modification and deletion)

s = MovingAverage(3)
print(s.next(1))
print(s.next(10))
print(s.next(3))
print(s.next(5))
print(s.next(4))

