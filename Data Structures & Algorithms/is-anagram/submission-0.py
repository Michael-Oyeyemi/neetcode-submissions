class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(x) == t.count(x) for x in set(list(s))) and len(s) == len(t)