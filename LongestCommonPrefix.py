#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jianyu Yang on 2021/8/8 21:02
"""


def longestCommonPrefix(strs: list) -> str:
    if not strs:
        return ""

    shortest = min(strs, key=len)

    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest


if __name__ == '__main__':
    longestCommonPrefix(["a", "ac"])
