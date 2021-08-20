# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 09:10
# @Author  : Yang Jianyu
# @File    : BackspaceStrComp.py
# @Software: LeetCode


# 844
def backspaceCompare(self, s: str, t: str) -> bool:
    s_stack, t_stack = [], []

    for char in s:
        if char == "#":
            if s_stack:
                s_stack.pop()
            continue
        else:
            s_stack.append(char)

    for char in t:
        if char == "#":
            if t_stack:
                t_stack.pop()
            continue
        else:
            t_stack.append(char)

    return s_stack == t_stack