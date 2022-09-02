# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left, right = 0, 0
        ans = 0
        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:
                hashset.remove(s[left])
                left += 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
