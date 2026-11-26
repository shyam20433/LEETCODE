class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set("aeiou")
        maxi=0
        for i in range(k):
            if s[i] in vowels:
                maxi+=1
        count=maxi
        print(maxi)
        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            maxi=max(count,maxi)
        return maxi
            
                