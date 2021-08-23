# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 09:18
# @Author  : Yang Jianyu
# @File    : BaseballGame.py
# @Software: LeetCode


def calPoints(self, ops: List[str]) -> int:
    score = []
    for op in ops:
        if op == "C":
            score.pop()
        elif op == "D":
            last_score = score.pop()
            curr_score = int(last_score) * 2
            score.append(last_score)
            score.append(curr_score)
        elif op == "+":
            score_one = score.pop()
            score_two = score.pop()
            curr_score = int(score_one) + int(score_two)
            score.extend([score_two, score_one, curr_score])
        else:
            score.append(int(op))
    return sum(score)