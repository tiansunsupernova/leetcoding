class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strings:
            encoder = []
            for ch in s:
                encoder.append(str((ord(ch) - ord(s[0])) % 26))
            groups["+".join(encoder)].append(s)
        return groups.values()
