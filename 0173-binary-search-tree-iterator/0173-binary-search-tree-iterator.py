# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack=[]
        self.push(root)
        

    def next(self) -> int:
        return self.stack.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.stack)!=0
    
    def push(self,root)-> list:
        if not root:
            return
        
        self.stack.append(root.val)
        if root.right:
            self.push(root.right)
        if root.left:
            self.push(root.left)
        self.stack=sorted(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()