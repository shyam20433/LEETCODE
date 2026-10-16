class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hash=defaultdict(int)
        for i in nums:
            hash[i]+=1
        hash=dict(sorted(hash.items(),key=lambda x:x[-1]))
        for k,v in hash.items():
            if v==1:
                return k
        return -1