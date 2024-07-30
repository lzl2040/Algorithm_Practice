# -*- encoding: utf-8 -*-
"""
File solution.py.py
Created on 2024/7/29 13:07
Copyright (c) 2024/7/29
@author: 
"""
class Solution_1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_s = 0
        for i in range(n):
            if i > max_s:
                return False
            max_s = max(i + nums[i], max_s)
        return True


class Solution_2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        dp = [0] * len(nums)
        # dp[i]表示从0-i任意一点出发，你可以到达的最远位置
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], i + nums[i])
            if dp[i] >= len(nums) - 1:
                return True

            # 0-i随便取一个最远能达到的也只是i，不符合
            if dp[i] == i:
                return False
        return True

