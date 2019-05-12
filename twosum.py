class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        for index in range(length):
            for i in range(index+1,length):
                if nums[i]+nums[index]==target:
                    return  [index,i]
                
                
