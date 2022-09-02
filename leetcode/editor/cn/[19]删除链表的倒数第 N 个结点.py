from playground import ListNode, list2link, print_link


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = ListNode(next=head)
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if slow.next == head:
            return slow.next.next
        else:
            slow.next = slow.next.next
            return head
# leetcode submit region end(Prohibit modification and deletion)


head = list2link([1, 2])
print_link(head)
ans = Solution().removeNthFromEnd(head, 1)
print_link(ans)