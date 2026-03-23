#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode.cn/problems/majority-element/description/
#
# 题目描述：
# 给定一个大小为 n 的数组 nums，返回其中的多数元素。
# 多数元素是指在数组中出现次数 严格大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例 1：
# 输入：nums = [3,2,3]
# 输出：3
#
# 示例 2：
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#
# 提示：
# - n == nums.length
# - 1 <= n <= 5 * 10^4
# - -10^9 <= nums[i] <= 10^9
# - 输入保证数组中一定有一个多数元素
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
#
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TODO: 初始化候选者和计数器
        # candidate 记录当前候选的多数元素
        # count 记录候选者的"票数"
        candidate = None

        count = 0
        
        # TODO: 遍历数组
        for num in nums:
            # TODO: 如果 count 为 0，说明之前都被抵消完了
            # 把当前元素设为新的 candidate，count 设为 1
            if count == 0:
               candidate = num 
               count += 1
            # TODO: 如果当前元素等于 candidate，count 加 1
            elif candidate == num :
                count+=1
            else:   
                count -= 1
                     
            # TODO: 如果当前元素不等于 candidate，count 减 1（抵消）
                    

            
            
            
        return candidate    
        # TODO: 返回最终的 candidate
        
# @lc code=end
