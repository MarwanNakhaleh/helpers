'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# my homemade solution
class Solution(object):
    def twoSumMarwan(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return "invalid!"
        if len(nums) == 2:
            return [0, 1]
        print(nums)
        for x in range(0, len(nums)):
            for y in range(1, len(nums)):
                if nums[x] + nums[y] == target and x != y:
                    return [x, y]
        return None
            
    def twoSumGood(self, nums, target):
        lookup = {}
        
        for i, num in enumerate(nums):
            if num in lookup:
                return [lookup[num], i]
            else:
                lookup[target-num] = i