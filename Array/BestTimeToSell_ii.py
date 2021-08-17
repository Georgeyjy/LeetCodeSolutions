# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 10:09
# @Author  : Yang Jianyu
# @File    : BestTimeToSell_ii.py
# @Software: LeetCode


def maxProfit(prices: list) -> int:
    max_profit = 0
    min_price = prices[0]

    for p in prices:
        min_price = min(p, min_price)
        if p > min_price:
            max_profit += p - min_price
            min_price = p

    return max_profit
