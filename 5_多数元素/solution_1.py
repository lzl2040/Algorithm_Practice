# -*- encoding: utf-8 -*-
"""
File solution_1.py
Created on 2024/5/24 0:07
Copyright (c) 2024/5/24
@author: 
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        j = 0
        n = int(len(nums) / 2)
        while i < len(nums):
            while nums[i] == nums[j]:
                j = j + 1
                if j >= len(nums):
                    break
            if j - i > n:
                return nums[i]
            i = j
        return nums[-1]


