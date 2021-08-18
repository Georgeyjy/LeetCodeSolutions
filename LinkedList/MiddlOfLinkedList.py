# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 09:21
# @Author  : Yang Jianyu
# @File    : MiddlOfLinkedList.py
# @Software: LeetCode


def middleNode(self, head: ListNode) -> ListNode:
    slow, fast = head, head
    while True:
        if head.next is None:
            return head
        elif head.next.next is None:
            return head.next

        slow = slow.next
        fast = fast.next.next

        if fast.next is None:
            return slow
        elif fast.next.next is None:
            return slow.next