# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 14:58
# @Author  : Yang Jianyu
# @File    : TwoSum_ii.py
# @Software: LeetCode


def twoSum(numbers: list, target: int) -> list:
    low, high = 0, len(numbers) - 1

    while low < high:
        total = numbers[low] + numbers[high]
        if target < total:
            high -= 1
        elif target > total:
            low += 1
        else:
            return [low + 1, high + 1]

    return [low + 1, high + 1]