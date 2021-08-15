#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jianyu Yang on 2021/8/15 16:35
"""


# 贪心 找到最低买入和最高卖出 每天都可能卖出，则在每天判断当日卖出的最大利润和历史最低价
# 循环一次
def maxProfit(prices: list) -> int:
    price_min = prices[0]
    res = 0

    for p in prices:
        price_min = min(price_min, p)
        res = max(res, p - price_min)

    return res
