from playground import ListNode, list2link, print_link


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# leetcode submit region end(Prohibit modification and deletion)


head = list2link([1,2,3,4,5])
print_link(head)
print(Solution().reverseList(head))