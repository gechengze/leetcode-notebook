from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if num <= d[mid]:
                        r = mid - 1
                        loc = mid
                    else:
                        l = mid + 1
                d[loc] = num

        return len(d)
# leetcode submit region end(Prohibit modification and deletion)


print(Solution().lengthOfLIS([0,1,0,3,2,3]))