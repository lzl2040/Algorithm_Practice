# 解决方案
## 题目内容
leetcode链接：[地址](https://leetcode.cn/problems/majority-element)

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
## 思路
- 思路1：先排序，然后指定两个指针i和j，i代表当前元素的开始位置，j表示结束位置（一直移动直到nums[i]!=nums[j]），判断j-i是否大于nums长度的一半
- 思路2：