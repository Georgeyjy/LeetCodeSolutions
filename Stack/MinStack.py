# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 09:18
# @Author  : Yang Jianyu
# @File    : MinStack.py
# @Software: LeetCode


# 155
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        for i, num in enumerate(self.stack):
            if i == len(self.stack) - 1:
                return num

    def getMin(self) -> int:
        min_int = self.stack[0]
        for i in self.stack:
            if i is None:
                continue
            else:
                min_int = i if i < min_int else min_int
        return min_int