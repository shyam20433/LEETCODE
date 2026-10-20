class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l=[0]*26
        for i in s:
            l[ord(i)-ord("a")]+=1
        for i in t:
            l[ord(i)-ord("a")]-=1
        for i in range(26):
            if l[i]!=0:
                return chr(i+97)
        