#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jianyu Yang on 2021/8/7 22:51
"""


# def romanToInt(self, s: str) -> int:
#     if len(s) == 0:
#         return 0
#     roman_int_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     roman_weight = {"I": 1, "V": 2, "X": 3, "L": 4, "C": 5, "D": 6, "M": 7}
#     res = 0
#
#     for idx, char in enumerate(s):
#         try:
#             if roman_weight[char] < roman_weight[s[idx + 1]]:
#                 res -= roman_int_map[char]
#             else:
#                 res += roman_int_map[char]
#         except:
#             res += roman_int_map[char]
#             break
#
#     return res

def romanToInt(self, s: str) -> int:
    roman_int_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    prev = 0

    for char in s[::-1]:
        curr = roman_int_map[char]
        if curr < prev:
            res -= curr
        else:
            res += curr
        prev = curr

    return res
