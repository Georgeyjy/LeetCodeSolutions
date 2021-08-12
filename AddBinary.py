#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jianyu Yang on 2021/8/12 22:04
"""


def addBinary(a: str, b: str) -> str:
    carry, i, j = 0, len(a) - 1, len(b) - 1
    res = ""

    # 从末位开始分别遍历两个字符串
    # 任意字符串某一位不为0时继续循环，超出字符串索引边界则为当前字符赋值0
    # 进位大于0时也继续循环，即将进位最终添加到最高位
    while carry > 0 or i >= 0 or j >= 0:
        int_a = 0 if i < 0 else int(a[i])
        int_b = 0 if j < 0 else int(b[j])
        char_sum = int_a + int_b + carry
        val = char_sum % 2
        carry = char_sum // 2
        res += str(val)
        j -= 1
        i -= 1
    # 反转字符串得到最终结果
    return res[::-1]
