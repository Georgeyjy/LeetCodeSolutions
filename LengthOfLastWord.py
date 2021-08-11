#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jianyu Yang on 2021/8/11 20:41
"""


def lengthOfLastWord(s: str) -> int:
    s = s[::-1]
    count = 0

    if len(s) == 1:
        return 1

    for i in range(len(s)):
        if s[i] != " ":
            count += 1
            if i == len(s) - 1 or s[i + 1] == " ":
                return count
    return 0


if __name__ == '__main__':
    lengthOfLastWord("Hello World")
