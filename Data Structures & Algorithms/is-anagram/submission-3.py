class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        slist = sorted(s)
        tlist = sorted(t)
        
        for x, y in zip(slist, tlist):
            if x != y:
                return False
        return True
        