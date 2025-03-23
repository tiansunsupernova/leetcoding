# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def __init__(self):
        self.target_node = None

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        newroot = self.dfs(root, target, None)
        q = deque([self.target_node])
        res = []
        visited = set()

        while q and k >= 0:
            cnt = len(q)
            for i in range(cnt):
                cur = q.popleft()
                if cur and cur.val not in visited:
                    visited.add(cur.val)
                    if k == 0: res.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
                    q.append(cur.parent)
            k -= 1
        return res

    

    def dfs(self, node, target, parent):
        if not node: return
        copy = Node(node.val)
        if node.val == target.val: 
            self.target_node = copy

        copy.parent = parent
        copy.left = self.dfs(node.left, target, copy)
        copy.right = self.dfs(node.right, target, copy)

        return copy
        