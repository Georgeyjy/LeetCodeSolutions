#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jianyu Yang on 2021/8/8 22:30
"""

def isValid(s: str) -> bool:
    if not s:
        return False
    stack = [0]
    paren_map = {"]": "[", "}": "{", ")": "("}

    for i in s:
        if i in paren_map.values():
            stack.append(i)
        elif i in paren_map and paren_map[i] != stack.pop():
            return False
    return stack == [0]
