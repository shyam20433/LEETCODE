class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        minimum=float('-inf')
        stack=[] #2 
        for i in nums[::-1]:
            if i<minimum:
                return True
            while stack and stack[-1]<i:
                minimum=stack.pop()
            stack.append(i)
        return False
        