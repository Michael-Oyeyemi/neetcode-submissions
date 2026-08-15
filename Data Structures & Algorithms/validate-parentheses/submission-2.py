class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        pairs = {")": "(", "}": "{", "]":'['}
        for char in s:
            if char not in pairs:
                stack.append(char)
                continue
            if char in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[char]:
                    return False
        return len(stack) == 0