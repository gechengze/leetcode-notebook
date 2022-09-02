from playground import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        p = head
        for _ in range(n // 2):
            p = p.next
        if n % 2 != 0:
            p = p.next
        prev, curr = None, p
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        p = head
        for _ in range(n // 2):
            if p.val != prev.val:
                return False
            p = p.next
            prev = prev.next
        return True

# leetcode submit region end(Prohibit modification and deletion)
