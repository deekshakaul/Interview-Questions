# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        j = 0
        numLength = len(nums)
        while i < numLength:
            if nums[i] == nums[j]:
                i += 1
            else:
                j+=1
                nums[j]=nums[i]
                i+=1
        while j < i-1:
            nums.pop()
            j+=1
        return len(nums)
                
        
