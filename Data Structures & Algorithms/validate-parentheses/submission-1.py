class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"]":"[", ")":"(", "}":"{"}
        for word in s:

            if word in match:
                if not stack:
                    return False
                d = stack.pop()
                if d != match[word]:
                    return False
            else:
                stack.append(word)

        if stack:
            return False

        return True