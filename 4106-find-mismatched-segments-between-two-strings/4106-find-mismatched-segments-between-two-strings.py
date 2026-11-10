class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res=[]
        i=0
        while i<len(s1):
            res1=""
            res2=""
            while i<len(s1) and s1[i]!=s2[i]:
                res1+=s1[i]
                res2+=s2[i]
                i+=1
            if res1 and res2:
                res.append([res1,res2])
            i+=1
        return res
        # res=[]
        # res1=""
        # res2=""
        # for i in range(len(s1)):
        #     if s1[i]!=s2[i]:
        #         res1+=s1[i]
        #         res2+=s2[i]
        #     else:
        #         if res1 and res2:
        #             res.append([res1,res2])
        #         res1=""
        #         res2=""
        # if res1 and res2:
        #     res.append([res1,res2])
        # return res
        