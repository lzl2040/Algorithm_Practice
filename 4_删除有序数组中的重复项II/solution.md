# 解决方案
## 题目内容
leetcode链接：[地址](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii)

给你一个有序数组 nums ，请你 **原地** 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

## 思路
- 思路1：维护三个指针，头指针head，尾指针tail以及当前元素的指针count
  - head记录相同元素的起始位置
  - tail指针不断移动，并比较和head指针的距离
  - count指针根据tail和head指针的距离进行移动
- 思路2：