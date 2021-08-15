# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 09:57
# @Author  : Yang Jianyu
# @File    : PlusOne.py
# @Software: LeetCode


def plusOne(digits: list) -> list:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        digits[i] %= 10
        if digits[i] != 0:
            return digits
    res = [1]
    res.extend(digits)
    return res
