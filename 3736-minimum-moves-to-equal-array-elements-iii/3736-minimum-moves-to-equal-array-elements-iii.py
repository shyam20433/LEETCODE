class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        maxi=max(nums)
        for i in nums:
            count+=maxi-i
        return count
        