class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        for i, sub in enumerate(s):
            dup = set()
            length = 0  
            for j in range(i, len(s)):
                if s[j] in dup:
                    break
                length += 1
                dup.add(s[j])

            max_length = max(max_length, length)
        return max_length