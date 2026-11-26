class Solution:
    def canAliceWin(self, n: int) -> bool:
        total=10*(10+1)//2
        moves=total-n
        unplayed=round(sqrt(2*moves))
        return unplayed%2==1

        # if n<10:
        #     return False
        # counter=10
        # while n and n>counter:
        #     n-=counter
        #     counter-=1
        # return n%2==0
        