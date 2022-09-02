from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.hashtable = {}
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hashtable[idKey] = value
        if idKey == self.ptr and self.ptr <= self.n:
            ret = []
            while idKey in self.hashtable.keys():
                ret.append(self.hashtable[idKey])
                idKey += 1
            self.ptr = idKey
            return ret
        else:
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# leetcode submit region end(Prohibit modification and deletion)


os = OrderedStream(5)
print(os.insert(3,'ccccc'))
print(os.insert(1,'aaaaa'))
print(os.insert(2,'bbbbb'))
print(os.insert(5,'eeeee'))
print(os.insert(4,'ddddd'))
