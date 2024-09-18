# -*- encoding: utf-8 -*-
"""
File solution.py.py
Created on 2024/7/29 13:07
Copyright (c) 2024/7/29
@author: 
"""


class Solution_1(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)

        index = 0
        for cite in citations:
            if index >= cite:
                break
            index += 1
        return index


