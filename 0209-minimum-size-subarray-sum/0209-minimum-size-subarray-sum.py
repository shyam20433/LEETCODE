class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total=0
        mini=float('inf')
        left=0
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                mini=min(mini,right-left+1)
                total-=nums[left]
                left+=1
            
        return mini if mini!=float('inf') else 0