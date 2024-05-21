# -*- encoding: utf-8 -*-
"""
File solution_1.py
Created on 2024/5/21 23:21
Copyright (c) 2024/5/21
@author: 
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            if nums[i] == val:
                nums.remove(val)
                nums_len = nums_len - 1
            else:
                i = i + 1
        return len(nums)