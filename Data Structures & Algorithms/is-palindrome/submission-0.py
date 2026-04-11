class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()

        for i in range(len(s)):
            print(s[i],s[len(s)-1-i] )
            if s[i] != s[len(s)-1-i]:
                return False
        return True