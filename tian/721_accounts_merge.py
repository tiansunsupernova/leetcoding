class Solution:
    def __init__(self):
        self.root = defaultdict(str)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        di = defaultdict(str) # key = email, value = name

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                x = account[i]
                di[x] = name
                if x not in self.root: self.root[x] = x
                self.union(x, account[1])

        childrens = defaultdict(list) # key = email, value = list of emails that has key as root

        for email in di.keys():
            childrens[self.find(email)].append(email)
        
        res = []
        for email in childrens.keys():
            cur = []
            cur.append(di[email])
            cur.extend(sorted(childrens[email]))
            res.append(cur)
        
        return res
    
    def find(self, x):
        if x not in self.root: self.root[x] = x
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot != yRoot:
            self.root[xRoot] = yRoot