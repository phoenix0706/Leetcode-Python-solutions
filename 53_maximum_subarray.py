'''
https://leetcode.com/problems/maximum-subarray/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_=0
        maxm=nums[0]
        for i in range(len(nums)):
            sum_+=nums[i]
            maxm=max(sum_,maxm)

            if sum_<0:
                sum_=0
           
        return maxm
        