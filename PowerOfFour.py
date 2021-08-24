# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 11:04
# @Author  : Yang Jianyu
# @File    : PowerOfFour.py
# @Software: LeetCode


# def isPowerOfFour(self, n: int) -> bool:
#     if n <= 0: return False
#     while n > 1:
#         n /= 4
#         if str(n).split(".")[1] != "0":
#             return False
#     return True

def isPowerOfFour(self, n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
