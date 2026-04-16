from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)

        for s in strs:
            k = "".join(sorted(s))
            dic[hash(k)].append(s)

        answer = []
        for k, l in dic.items():
            answer.append(l)
        
        print(dic)
        return answer
            