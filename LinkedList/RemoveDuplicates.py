# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 18:35
# @Author  : Yang Jianyu
# @File    : RemoveDuplicates.py
# @Software: LeetCode


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head is None: return head
    curr = head
    while curr is not None:
        if curr.next is None: return head
        if curr.next.val == curr.val:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = None
        else:
            curr = curr.next
    return head