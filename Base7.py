# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 11:07
# @Author  : Yang Jianyu
# @File    : Base7.py
# @Software: LeetCode


def convertToBase7(num: int) -> str:
    if not num:
        return "0"
    usign_n = abs(num)
    res = ""
    while usign_n:
        val = usign_n % 7
        res += str(val)
        usign_n //= 7
    return res[::-1] if num > 0 else "-" + res[::-1]
