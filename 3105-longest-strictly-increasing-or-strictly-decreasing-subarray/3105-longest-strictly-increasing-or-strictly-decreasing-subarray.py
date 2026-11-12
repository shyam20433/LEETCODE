class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi=1
        count=1
        mini=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                count=1
            maxi=max(maxi,count)
        count=1
        for i in range(len(nums)-2,-1,-1):
            print(i,nums[i])
            if nums[i]>nums[i+1]:
                print(True)
                count+=1
            
            else:
                count=1
            mini=max(mini,count)
        return max(mini,maxi)