#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# 题目描述：
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
# 示例 1:
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# 示例 2:
# 输入: numRows = 1
# 输出: [[1]]
#
# 提示:
# - 1 <= numRows <= 30
#
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 方法：逐行构建，每行根据上一行计算
        
        # TODO: 初始化结果列表
        result = []
        
        # TODO: 循环生成第 1 行到第 numRows 行
        for i in range(numRows):
            # TODO: 创建当前行，初始时所有元素都是 1
            # 第 i 行有 i+1 个元素（行号从0开始）
            row = [1] * (i+1)
            
            # TODO: 填充当前行的中间元素（如果有的话）
            # 中间元素（索引 1 到 i-1）= 上一行左上方 + 上一行右上方
            # 即：row[j] = result[i-1][j-1] + result[i-1][j]
            # 注意：只有 i >= 2（第3行及以后）才需要计算中间元素
            if i>=2:
                for j in range(1,i):
                    row[j] = result[i-1][j-1] + result[i-1][j]
                # TODO: 遍历中间位置，计算每个位置的值
            result.append(row)    
                
            # TODO: 把当前行加入结果列表
            
        return result    
        # TODO: 返回结果列表
        
# @lc code=end
