# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 10:51
# @Author  : Yang Jianyu
# @File    : MaximumNumberOfBalloons.py
# @Software: LeetCode


def maxNumberOfBalloons(self, text: str) -> int:
    char_count = {}
    for char in text:
        char_count.setdefault(char, 0)
        char_count[char] += 1
    b = char_count.get("b")
    a = char_count.get("a")
    l = char_count.get("l")
    o = char_count.get("o")
    n = char_count.get("n")
    if not all([b, a, l, o, n]):
        return 0
    text.count()
    return min(l // 2, o // 2, b, a, n)
