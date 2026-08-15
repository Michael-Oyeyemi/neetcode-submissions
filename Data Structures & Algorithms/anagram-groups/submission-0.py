class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            counts = tuple(counts)
            if counts in groups:
                groups[counts].append(word)
            else:
                groups[counts] = [word]
        
        return list(groups.values())