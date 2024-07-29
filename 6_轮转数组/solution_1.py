# -*- encoding: utf-8 -*-
"""
File solution_1.py
Created on 2024/5/24 0:07
Copyright (c) 2024/5/24
@author: 
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            return nums
        pos = k % len(nums)
        right = nums[len(nums) - pos: len(nums)]
        left = nums[:len(nums) - pos]
        nums[:pos] = right
        nums[pos:] = left
        return nums


