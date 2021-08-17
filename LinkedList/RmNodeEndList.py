# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 19:16
# @Author  : Yang Jianyu
# @File    : RmNodeEndList.py
# @Software: LeetCode


# TODO： 其他更优解
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    def get_full_length(head: ListNode):
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    dummy = ListNode(0, head)
    l = get_full_length(dummy)
    count = 0
    curr = dummy
    target = l - n + 1

    while curr is not None:
        count += 1
        if count + 1 == target:
            prev = curr
        if count == target:
            prev.next = curr.next
            curr.next = None
            break
        curr = curr.next

    return dummy.next