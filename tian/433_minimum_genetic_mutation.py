class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        seen = {startGene}

        while q:
            cur, steps = q.popleft()
            if cur == endGene: return steps
            for c in "ACGT":
                for i in range(len(cur)):
                    candidate = cur[:i] + c + cur[i+1:]
                    if candidate not in seen and candidate in bank:
                        q.append((candidate, steps + 1))
                        seen.add(candidate)
        return -1
