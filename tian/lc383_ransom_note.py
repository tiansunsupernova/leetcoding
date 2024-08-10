import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False

        m_counts = collections.Counter(magazine)
        r_counts = collections.Counter(ransomNote)

        for c, r_cnt in r_counts.items():
            if c not in m_counts or r_cnt > m_counts[c]:
                return False
        
        return True
            
