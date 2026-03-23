#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/
#
# 题目描述：
# 给定一个数组 prices，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。
# 设计一个算法来计算你所能获取的最大利润。
# 
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0。
#
# 示例 1：
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，
#      最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
# 示例 2：
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下，没有交易完成，所以最大利润为 0。
#
# 提示：
# - 1 <= prices.length <= 10^5
# - 0 <= prices[i] <= 10^4
#
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 方法：一次遍历，维护最低买入价格和最大利润
        # 核心思路：对于每一天，如果今天卖出，最优的买入时机是之前价格最低的那天
        
        # TODO: 初始化最小价格为无穷大（或 prices[0]）
        # min_price 记录遍历到目前为止看到的最低价格
        min_price = prices[0]
       
        # TODO: 初始化最大利润为 0
        # 如果全程没有正利润，就返回 0（表示不交易）
        max_profit = 0
        
        # TODO: 遍历每一天的价格
        for price in prices:

            if price < min_price:
                min_price = price
            else:
                tem = price - min_price
                if tem > max_profit:
                    max_profit = tem
            

            
            
        # TODO: 返回 max_profit
        return max_profit
        
# @lc code=end
