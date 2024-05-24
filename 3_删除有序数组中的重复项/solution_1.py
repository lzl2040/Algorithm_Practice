# -*- encoding: utf-8 -*-
"""
File solution_1.py
Created on 2024/5/24 0:07
Copyright (c) 2024/5/24
@author: 
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        i = 0
        while i < nums_len - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
                nums_len = nums_len - 1
                continue
            i = i + 1
        return len(nums)



