# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 09:19
# @Author  : Yang Jianyu
# @File    : QueueUsingStack.py
# @Software: LeetCode


# 232
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        ret = self.queue[0]
        if ret is None:
            return ret
        self.queue.remove(ret)
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if len(self.queue) == 0 else False