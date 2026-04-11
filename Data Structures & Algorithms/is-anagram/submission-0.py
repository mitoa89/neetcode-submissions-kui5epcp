class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sSort = list(s)
        
        tSort = list(t)
        
        print(sSort.sort())
        print(tSort.sort())
        return sSort == tSort;