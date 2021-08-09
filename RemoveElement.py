# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 10:44
# @Author  : Yang Jianyu
# @File    : RemoveElement.py
# @Software: LeetCode

# 双指针

def removeElement(nums: list, val: int) -> int:
    idx = 0
    for i in nums:
        if i != val:
            nums[idx] = i
            idx += 1
    return idx


# def removeElement(self, nums: List[int], val: int) -> int:
#     res = len(nums)
#     while True:
#         try:
#             nums.remove(val)
#             nums.append("_")
#             res -= 1
#         except:
#             break
#     return res
