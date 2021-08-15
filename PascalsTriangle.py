#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jianyu Yang on 2021/8/15 15:53
"""


def generate(numRows: int) -> List[List[int]]:
    res = [[1]]
    line = [1]
    for i in range(0, numRows - 1):
        line = [0] + line + [0]
        new_line = []
        for j in range(0, len(line) - 1):
            new_line.append(line[j] + line[j + 1])
        res.append(new_line)
        line = new_line
    return res


if __name__ == '__main__':
    generate(5)