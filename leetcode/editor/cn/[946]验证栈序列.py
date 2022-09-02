from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, j = [], 0
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return len(st) == 0

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(Solution().validateStackSequences([1,0], [1,0]))