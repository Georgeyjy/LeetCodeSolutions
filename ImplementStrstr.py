# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 09:01
# @Author  : Yang Jianyu
# @File    : ImplementStrstr.py
# @Software: LeetCode
# https://leetcode-cn.com/problems/implement-strstr/


# TODO: KMP算法
def strStr(haystack: str, needle: str) -> int:
    l = len(needle)

    if not needle:
        return 0

    for i in range(len(haystack)):
        if haystack[i:i+l] == needle and i + l <= len(haystack):
            return i
    return -1


if __name__ == '__main__':
    strStr("hello", "ll")
