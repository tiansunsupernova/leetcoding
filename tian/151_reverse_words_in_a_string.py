class Solution:
    def reverseWords(self, s: str) -> str:
        li = [word for word in s.strip().split(" ") if word]
        li.reverse()
        return " ".join(li)
