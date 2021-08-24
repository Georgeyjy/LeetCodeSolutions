# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 10:43
# @Author  : Yang Jianyu
# @File    : FlattenNested.py
# @Software: LeetCode


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested = nestedList
        self.i = 0
        self.iter = None
        self.size = len(nestedList) if nestedList else 0

    def next(self) -> int:
        curr = self.nested[self.i]
        if curr.isInteger():
            self.i += 1
            return curr.getInteger()
        else:
            return self.iter.next()

    def hasNext(self) -> bool:
        while self.i < self.size:
            curr = self.nested[self.i]
            if curr.isInteger():
                return True
            else:
                if self.iter is None:
                    self.iter = NestedIterator(curr.getList())
                if self.iter.hasNext():
                    return True
                else:
                    self.iter = None
                    self.i += 1
        return False
