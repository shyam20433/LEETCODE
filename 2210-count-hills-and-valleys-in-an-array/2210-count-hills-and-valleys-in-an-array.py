class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        count=0
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i-1]:
                continue
            if nums[i-1]<nums[i]>nums[i+1] or nums[i-1]>nums[i]<nums[i+1]:
                count+=1
            else:
                next=i+1
                while next<len(nums)-1 and nums[i]==nums[next]:
                    next+=1
                if nums[i-1]<nums[i]>nums[next] or nums[i-1]>nums[i]<nums[next]:
                    count+=1
        return count
            
        