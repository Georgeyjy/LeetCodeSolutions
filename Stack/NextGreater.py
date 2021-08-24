# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 17:25
# @Author  : Yang Jianyu
# @File    : NextGreater.py
# @Software: LeetCode


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    res, tmp = [], []

    def recover_nums2():
        while tmp:
            nums2.append(tmp.pop())

    for i in nums1:
        num = -1
        recover_nums2()
        while nums2:
            last = nums2.pop()
            tmp.append(last)
            if last == i:
                break
            num = last if last > i else num
        res.append(num)
    return res


if __name__ == '__main__':
    nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
