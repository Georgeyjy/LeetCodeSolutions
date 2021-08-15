# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 09:47
# @Author  : Yang Jianyu
# @File    : MaximumSubarray.py
# @Software: LeetCode


def maxSubArray(nums: list) -> int:
    res = nums[0]

    for i in range(1, len(nums)):
        s = nums[i] + nums[i - 1]
        if s > nums[i]:
            nums[i] = s
        if nums[i] > res:
            res = nums[i]

    return res
