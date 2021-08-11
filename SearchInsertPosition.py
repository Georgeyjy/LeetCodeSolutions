# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 09:34
# @Author  : Yang Jianyu
# @File    : SearchInsertPosition.py
# @Software: LeetCode


# 二分查找
def searchInsert(nums: list, target: int) -> int:
    lo, mid = 0, 0
    hi = len(nums) - 1

    if target > nums[hi]:
        return hi + 1
    if target < nums[lo]:
        return 0

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid
        else:
            return mid
    return lo


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 7))