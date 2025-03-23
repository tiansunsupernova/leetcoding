class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        words = sentence.split(" ")
        res = []

        for i, w in enumerate(words):
            if w[0] in vowels:
                res.append(w + "ma")
            else:
                res.append(w[1:] + w[0] + "ma")
            res[-1] += 'a' * (i + 1)
        
        return " ".join(res)
