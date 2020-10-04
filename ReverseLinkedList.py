# problem url: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr, pre = head, None
        while curr is not None:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre
