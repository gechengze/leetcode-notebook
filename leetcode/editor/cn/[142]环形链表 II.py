from playground import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        hashset = set()
        while head:
            if head in hashset:
                return head
            hashset.add(head)
            head = head.next

        return None
        
# leetcode submit region end(Prohibit modification and deletion)
