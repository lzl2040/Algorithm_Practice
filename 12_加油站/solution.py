# -*- encoding: utf-8 -*-
"""
File solution.py.py
Created on 2024/7/29 13:07
Copyright (c) 2024/7/29
@author: 
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        zhan_remain = [0] * n
        total = 0
        for i in range(n):
            zhan_remain[i] = gas[i] - cost[i]
            total += zhan_remain[i]

        if total < 0:
            return -1
        num = zhan_remain[0]
        head = 1
        tail = 0
        while tail != head and head < n:
            if num > 0:
                # 向右边扩充
                num += zhan_remain[head]
                head = (head + 1) % n
            else:
                # 尾节点从另外一个方向扩展
                tail = (n + tail - 1) % n
                num += zhan_remain[tail]

        return tail








