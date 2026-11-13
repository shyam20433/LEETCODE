# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        def decimal(nums):
            total=0
            p=0
            for i in nums[::-1]:
                if i=="1":
                    total+=2**p
                p+=1
            return total
        res=""
        curr=head
        while curr:
            res+=str(curr.val)
            curr=curr.next
        return decimal(res)
        