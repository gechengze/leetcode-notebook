# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
# leetcode submit region end(Prohibit modification and deletion)
