# 解决方案
## 题目内容
leetcode链接：[地址](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii)

给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
## 思路
- 思路一：找数组中的递增子序列，然后取其开始元素买入，结束元素卖出
- 思路二：贪心：只要第二天比第一天的高就买入，然后第二天卖出（没想到这个）
- 思路三：动态规划（下次领悟）