# -*- encoding: utf-8 -*-
"""
File solution.py.py
Created on 2024/7/29 13:07
Copyright (c) 2024/7/29
@author: 
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre_sum, post_sum = [0] * n, [0] * n
        res = [0] * n
        pre_sum[0] = 1
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] * nums[i - 1]

        post_sum[n - 1] = 1
        for i in range(n - 2, -1, -1):
            post_sum[i] = post_sum[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = pre_sum[i] * post_sum[i]
        return res



