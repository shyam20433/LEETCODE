class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for word in words:
            sum=0
            for c in word:
                sum+=weights[ord(c)-ord('a')]
            
            sum%=26
            res+=chr(ord('z')-sum)
        return res