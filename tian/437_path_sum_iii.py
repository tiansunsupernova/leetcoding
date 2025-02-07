# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0
        self.di = defaultdict(int) # k = csum, v = rep

    def traverse(self, node, target, csum):
        if not node: return 0
        
        csum += node.val

        if csum == target:
            self.cnt += 1

        # target = csum - prev_csum
        if csum - target in self.di:
            self.cnt += self.di[csum - target]
        self.di[csum] += 1


        self.traverse(node.left, target, csum)
        self.traverse(node.right, target, csum)

        self.di[csum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.traverse(root, targetSum, 0)
        return self.cnt