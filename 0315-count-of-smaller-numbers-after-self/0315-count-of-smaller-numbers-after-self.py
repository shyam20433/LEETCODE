class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n=len(nums)
        hash=[[num,i] for i,num in enumerate(nums)]
        res=[0]*n
        def split(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=split(nums[:mid])
            right=split(nums[mid:])
            return mergeSort(left,right)
        
        def mergeSort(left,right):
            sortedNums=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i][0]>right[j][0]:
                    # here why len(right) -j means => right will be always sorted in descending order before merge sort for example
                    # input [2,0,3] => [2] [0 ,3]=>left =[2] and right =>[3,0] so left[right] here will be 3 not 0 so 2<3 so right+=1
                    res[left[i][1]]+=len(right)-j
                    sortedNums.append(left[i])
                    i+=1
                else:
                    sortedNums.append(right[j])
                    j+=1
            while i<len(left):
                sortedNums.append(left[i])
                i+=1
            while j<len(right):
                sortedNums.append(right[j])
                j+=1
            return sortedNums
        split(hash)
        return res