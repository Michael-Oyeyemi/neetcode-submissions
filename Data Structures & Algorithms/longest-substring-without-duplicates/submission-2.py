class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        highest = 0
        seen = {}
        start = 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1
            seen[s[i]] = i
            highest = max(highest, i - start + 1)
        
        return highest