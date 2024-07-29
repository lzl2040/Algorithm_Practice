# -*- encoding: utf-8 -*-
"""
File solution.py.py
Created on 2024/7/29 13:07
Copyright (c) 2024/7/29
@author: 
"""
class Solution_1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_t = 0
        sell_t = 0
        start_dec = False
        num = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] <= prices[i]:
                if i != 0 and start_dec == True:
                    sell_t = i
                    num += (prices[sell_t] - prices[buy_t])
                    start_dec = False
            else:
                if start_dec == False:
                    start_dec = True
                    buy_t = i
                if i + 1 == len(prices) - 1:
                    num += (prices[i+1] - prices[buy_t])
        return num

class Solution_2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num = 0
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
                num += (prices[i+1] - prices[i])
                i = i + 1
        return num