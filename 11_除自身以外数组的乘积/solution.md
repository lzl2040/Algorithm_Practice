# 解决方案
## 题目内容
leetcode链接：[地址](https://leetcode.cn/problems/product-of-array-except-self)

时间：9-19

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
## 思路

- 思路一：顺序和逆序计算前缀和，然后计算某个下标对应的值时，两者相乘即可