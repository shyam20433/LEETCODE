class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        count=0
        for i in range(1,len(nums)):
            if  nums[i]==nums[i-1]:
                count+=1
        return count

        