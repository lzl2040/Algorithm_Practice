# -*- encoding: utf-8 -*-
"""
File solution.py.py
Created on 2024/7/29 13:07
Copyright (c) 2024/7/29
@author: 
"""
class Solution_1(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        i = 0
        min_s = 0
        while i < n:
            # 遍历从i出发能达到的点
            max_p = -1
            next_p = i + 1
            if i + nums[i] >= n - 1:
                min_s += 1
                return min_s
            for j in range(i + 1, i + 1 + nums[i]):
                p = j + nums[j]
                if p >= n - 1:
                    min_s += 2
                    return min_s
                if max_p < p:
                    max_p = p
                    next_p = j
            i = next_p
            min_s += 1
        return min_s

class Solution_2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_d = 0
        step = 0
        # 记录边界
        border = 0
        for i in range(n - 1):
            # 记录能达到的最远距离
            max_d = max(max_d, i + nums[i])
            if i == border:
                border = max_d
                step += 1
        return step


