class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        right=0
        for i in range(len(word)):
            if word[i]==ch:
                right=i
                break
        
        left=0
        #right
        word=list(word)
        while left<=right:
            temp=word[right]
            word[right]=word[left]
            word[left]=temp
            left+=1
            right-=1
        return "".join(word)
        