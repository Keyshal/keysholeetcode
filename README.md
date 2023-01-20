# keysholeetcode
用来记录leetcode的刷题记录

demo1.py BM63 跳台阶 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。这个其实是动态规划里面的组合方法的多少的问题.

demo2.py BM64 最小代价爬楼梯 cost[i]  是从楼梯第i 个台阶向上爬需要支付的费用，下标从0开始。一旦你支付此费用，即可选择向上爬一个或者两个台阶。你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。请你计算并返回达到楼梯顶部的最低花费。这个其实是前i-1 和前i-2里面记录的一直是最低消费.

demo3.py BM65 给定两个字符串str1和str2，输出两个字符串的最长公共子序列。如果最长公共子序列为空，则返回"-1"。目前给出的数据，仅仅会存在一个最长的公共子序列[输出这个公共子序列],其实这个里面分为两部分,其中一部分是dp制作而另一部分是根据dp来回溯序列.

demo4.py BM66 给定两个字符串str1和str2,输出两个字符串的最长公共子串 题目保证str1和str2的最长公共子串存在且唯一。[结果正确超时版本] 

demo5.py BM67 一个机器人在m×n大小的地图的左上角（起点）。机器人每次可以向下或向右移动。机器人要到达地图的右下角（终点）。可以有多少种不同的路径从起点走到终点？

demo6.py BM68 矩阵的最小和 给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。

demo7.py BM69 有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。现在给一串数字，返回有多少种可能的译码结果[只过了90%的用例].
