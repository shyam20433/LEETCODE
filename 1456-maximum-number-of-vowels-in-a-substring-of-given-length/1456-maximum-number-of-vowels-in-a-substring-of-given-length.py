class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set("aeiou")
        maxi=0
        res=[]
        for i in range(k):
            if s[i] in vowels:
                maxi+=1
            res.append(s[i])
        count=maxi
        print(maxi)
        for i in range(k,len(s)):
            if res and res[0] in vowels:
                count-=1
            res.pop(0)
            if s[i] in vowels:
                count+=1
            res.append(s[i])
            #print(s[i],count)
            #print(res)
            maxi=max(count,maxi)
        return maxi
            
                