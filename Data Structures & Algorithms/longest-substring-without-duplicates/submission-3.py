class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        length = 0
        dupdic = defaultdict(int)
        left = 0
        for i, sub in enumerate(s):
            if sub in dupdic and dupdic[sub] >= left:
                left = dupdic[sub] + 1

            length = i - left + 1
            print(length, sub, dupdic)
            dupdic[sub] = i
            max_length = max(max_length, length)

        return max_length