class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Dic 
        dic = {}

        for s in strs:
            # hash or sort? 
            # all lower case?
            s_key = str(sorted(s))
            if s_key in dic:
                dic[s_key].append(s)
            else:
                dic[s_key] = [s]
        
        answer = []
        for key, val in dic.items():
            answer.append(val)

        return answer
            