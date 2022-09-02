from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = curr = ListNode()
        carry = 0
        while l1 and l2:
            carry, temp = divmod(l1.val + l2.val + carry, 10)
            curr.next = ListNode(temp)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        p = l1 if l1 else l2
        while p:
            carry, temp = divmod(p.val + carry, 10)
            curr.next = ListNode(temp)
            curr = curr.next
            p = p.next

        if carry:
            curr.next = ListNode(1)
            curr = curr.next
        curr.next = None

        return ans.next

# leetcode submit region end(Prohibit modification and deletion)
