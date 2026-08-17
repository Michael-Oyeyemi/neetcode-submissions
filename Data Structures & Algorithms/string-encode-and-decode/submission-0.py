class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f"{len(word)}#{word}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        p1 = 0
        p2 = 0
        strs = []
        while p1 < len(s):
            while s[p2] != "#":
                p2 += 1
            length = int(s[p1:p2])
            strs.append(s[p2+1:p2+length+1])
            p1 = p2 = p2 + length + 1

        return strs


