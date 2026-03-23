#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# 给定一个长度为 n 的整数数组 height。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i])。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。
#
# 示例 1:
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
# 解释: 第1条线和第8条线之间的容器容量为 min(8,7) * (8-1) = 7 * 7 = 49
#
# 示例 2:
# 输入: height = [1,1]
# 输出: 1
#
# 提示:
# - n == height.length
# - 2 <= n <= 10^5
# - 0 <= height[i] <= 10^4
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
# @lc code=end
