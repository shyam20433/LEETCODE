class Solution:
    def validPalindrome(self, s: str) -> bool:

        # type -1 failed
        # word1=s
        # word2=s[::-1]
        # count=0
        # for i in range(len(s)):
        #     if word1[i]!=word2[i]:
        #         count+=1
        # return count==0 or count==1

        # type 2 failed
        # hash=Counter(s)
        # odd=0
        # for k,v in hash.items():
        #     if v%2:
        #         odd+=1
        # return odd<=2

        # type 3 Failed
        # n=len(s)
        # mid=n//2
        # def check(left,right):
        #     count=0
        #     while left>=0 and right<n:
        #         if s[left]!=s[right]:
        #             count+=1
        #         left-=1
        #         right+=1
                
        #     return count
        
        # if n%2:
        #     return check(mid,mid)==1
        # return check(mid-1,mid)==1

        # type 4 -success
        def checkPallindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return checkPallindrome(left+1,right) or checkPallindrome(left,right-1)
            left+=1
            right-=1
        return True