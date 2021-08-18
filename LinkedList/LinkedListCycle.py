# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 19:59
# @Author  : Yang Jianyu
# @File    : LinkedListCycle.py
# @Software: LeetCode


def hasCycle(self, head: ListNode) -> bool:
    if not head:
        return False

    fast = head.next
    slow = head

    if fast is None or slow is None:
        return False

    while fast is not None and slow is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True

    return False