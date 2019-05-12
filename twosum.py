class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index,num in enumerate(nums):
            for i in range(index+1,len(nums)):
                if nums[i]+nums[index]==target:
                    return  [index,i]
                
                
