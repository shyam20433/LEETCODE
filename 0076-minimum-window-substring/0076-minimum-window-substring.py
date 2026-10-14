class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        word_2=Counter(t)
        word1=defaultdict(int)
        res=""
        for right in range(len(s)):
            word1[s[right]]+=1
            while all(k in word1 and word1[k]>=v for k,v in word_2.items()):
                sub=s[left:right+1]
                if not res:
                    res=sub
                if len(sub)<len(res):
                    res=sub
                
                word1[s[left]]-=1
                if word1[s[left]]==0:
                    word1.pop(s[left])
                left+=1
        return res
        