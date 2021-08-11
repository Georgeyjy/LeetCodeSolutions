# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 09:39
# @Author  : Yang Jianyu
# @File    : RemoveDuplicatesFromSortedArray.py
# @Software: LeetCode

# 双指针 一个记录当前需要更改的索引，一个记录当前遍历的元素

def removeDuplicates(nums: list) -> int:
    idx = 0
    prev = None

    for i in nums:
        if i != prev:
            nums[idx] = i
            idx += 1
            prev = i
        continue

    return idx

# 利用python set特性去重

# def removeDuplicates(self, nums: List[int]) -> int:
#     removed = sorted(list(set(nums)))
#     nums[:len(removed)] = removed
#     return len(removed)
