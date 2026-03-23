#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode.cn/problems/single-number/description/
#
# 题目描述：
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。
# 找出那个只出现了一次的元素。
#
# 要求：
# - 线性时间复杂度 O(n)
# - 只使用常量额外空间 O(1)
#
# 示例 1：
# 输入：nums = [2,2,1]
# 输出：1
#
# 示例 2：
# 输入：nums = [4,1,2,1,2]
# 输出：4
#
# 示例 3：
# 输入：nums = [1]
# 输出：1
#
# 提示：
# - 1 <= nums.length <= 3 * 10^4
# - -3 * 10^4 <= nums[i] <= 3 * 10^4
# - 除了某个元素只出现一次以外，其余每个元素均出现两次
#
# 进阶：能否用位运算解决？
#
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TODO: 初始化 result，初始值应该是什么？
        result = 0
        
        # TODO: 遍历 nums，用异或运算更新 result
        # 提示：a ^ a = 0, a ^ 0 = a
        for num in nums :
            result = result ^ num
        
        # TODO: 返回 result
        return result
# @lc code=end
