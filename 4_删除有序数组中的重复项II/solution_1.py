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
        head = 0
        tail = 0
        count = 0
        while tail < len(nums):
            while nums[tail] == nums[head]:
                if tail - head < 2:
                    nums[count] = nums[head]
                    count = count + 1
                tail = tail + 1
                if tail >= len(nums):
                    return count
            nums[count] = nums[tail]
            count = count + 1
            head = tail
            tail = tail + 1
        return count
