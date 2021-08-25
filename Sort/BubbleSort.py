# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 18:37
# @Author  : Yang Jianyu
# @File    : BubbleSort.py
# @Software: LeetCode


def sortArray(self, nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        # 趟
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
