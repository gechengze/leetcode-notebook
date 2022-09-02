# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.queue = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue.insert(0, value)
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue.pop()
            return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.queue[0]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.queue[-1]

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.max



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
