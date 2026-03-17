#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
# 示例 1：
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
# 示例 3：
# 输入：nums = [1,0,1,2]
# 输出：3
#
# 提示：
# - 0 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9
#
# 进阶：你可以设计并实现时间复杂度为 O(n) 的算法吗？
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxlen = 0
        for num in nums_set:
            if num-1 in nums_set:
                continue

            cur_num = num
            cur_len = 1

            while cur_num + 1 in nums_set:
                cur_num += 1
                cur_len += 1
            maxlen = max(maxlen,cur_len)
        return maxlen

        
# @lc code=end
