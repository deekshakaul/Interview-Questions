# https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        nums = sorted(nums)
        length = len(nums)
        # precompute results for edge cases
        if length<4:
            return []
        if length == 4 and sum(nums) != target:
            return []
        if nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
            return []
        elif nums[0] + nums[1] + nums[2] + nums[3] > target:
            return []
        result = []
        for i in range(0, length - 3):
            for j in range(i+1, length-2):
                pending = target-nums[i]-nums[j]
                l = j+1
                r=length-1
                while l<r:
                    if nums[l] + nums[r] == pending:
                        subarray = [nums[i], nums[j], nums[l], nums[r]]
                        if subarray not in result:
                            result.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1
                    elif nums[l] + nums[r] < pending:
                        l+=1
                    else:
                        r-=1
        return result
                    
        
