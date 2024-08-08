class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    
        #Approach 1: with O(n^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target-nums[i] == nums[j]:
                    return i,j
        """
        #Approach 2: with O(n)
        indices = {}
        for i in range(len(nums)):
            if target - nums[i] in indices:
                return i,indices[target-nums[i]]
            else:
                indices[nums[i]]=i
