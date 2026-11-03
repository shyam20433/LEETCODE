class Solution:
    def findPoisonedDuration(self, nums: list[int], duration: int) -> int:
        # res=set()
        # for t in timeSeries:
        #     for j in range(t,t+duration):
        #         res.add(j)
        #         print(j)
        # return len(res)

        total=0
        for i in range(1,len(nums)):
            total+=min(duration,nums[i]-nums[i-1])
        return total+duration
