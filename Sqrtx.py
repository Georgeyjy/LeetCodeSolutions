# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 09:22
# @Author  : Yang Jianyu
# @File    : Sqrtx.py
# @Software: LeetCode


def mySqrt(x: int) -> int:
    if not x:
        return 0

    lo = 0
    hi = x
    mid = 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        mid = mid if mid > 0 else 1
        if mid ** 2 < x:
            if (mid + 1) ** 2 > x:
                return mid
            lo = mid + 1
        elif mid ** 2 > x:
            hi = mid
        else:
            return mid
    return mid


if __name__ == '__main__':
    mySqrt(255)
