class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        nums=[]
        for word in s:
            if word.isdigit():
                nums.append(int(word))
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                return False
        return True

        