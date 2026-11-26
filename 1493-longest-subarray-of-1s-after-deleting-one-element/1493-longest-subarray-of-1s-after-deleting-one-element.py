class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxi=0
        left=0
        zero=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            while zero>1:
                if nums[left]==0:
                    zero-=1
                left+=1
            maxi=max(maxi,right-left)
        return maxi
        