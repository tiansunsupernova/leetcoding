class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sorting
        citations.sort()
        for i, x in enumerate(citations):
            if x >= len(citations) - i:
                return len(citations) - i
        return 0