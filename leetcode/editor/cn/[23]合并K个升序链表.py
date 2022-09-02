from playground import ListNode
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        arr = []
        for head in lists:
            while head:
                arr.append(head)
                head = head.next
        if not arr:
            return None

        arr.sort(key=lambda x: x.val)
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        arr[-1].next = None
        return arr[0]
# leetcode submit region end(Prohibit modification and deletion)
