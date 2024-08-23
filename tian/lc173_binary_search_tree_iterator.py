# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.node = root
        if root: self.st.append(root)
        self.moveLeft()


    def next(self) -> int:
        old_val = self.node.val
        if self.node.right:
            self.node = self.node.right
            self.moveLeft()
            return old_val
        else:
            self.node = self.st.pop()
            return old_val

    def hasNext(self) -> bool:
        return bool(self.st)
        
    def moveLeft(self) -> None:
        while self.node.left:
            self.st.append(self.node)
            self.node = self.node.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()