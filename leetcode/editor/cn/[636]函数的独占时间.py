from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        st = []
        for log in logs:
            idx, tp, timestamp = log.split(':')
            idx, timestamp = int(idx), int(timestamp)
            if tp[0] == 's':
                if st:
                    ans[st[-1][0]] += timestamp - st[-1][1]
                    st[-1][1] = timestamp
                st.append([idx, timestamp])
            else:
                i, t = st.pop()
                ans[i] += timestamp - t + 1
                if st:
                    st[-1][1] = timestamp + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
