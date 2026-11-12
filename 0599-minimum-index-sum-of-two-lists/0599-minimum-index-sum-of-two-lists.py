class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        hash1={name:i for i,name in enumerate(list1)}
        hash2={name:i for i,name in enumerate(list2)}
        list2=set(list2)
        res=[]
        hash3={}
        for word in list1:
            if word in list2:
                length=abs(hash1[word]+hash2[word])
                hash3[word]=length
        mini=min(hash3.values())
        for k,v in hash3.items():
            if v==mini:
                res.append(k)
        return res

        