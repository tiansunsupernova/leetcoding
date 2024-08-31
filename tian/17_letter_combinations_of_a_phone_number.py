class Solution:
    def __init__(self):
        self.res = []
        self.letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []        
    
        self.btrack(0, [], digits)
        return self.res

    def btrack(self, i:int, li:List[int], digits: str):
        if i == len(digits): 
            self.res.append("".join(li))
            return
        for c in self.letters[digits[i]]:
            li.append(c)
            self.btrack(i+1, li, digits)
            li.pop()
        
