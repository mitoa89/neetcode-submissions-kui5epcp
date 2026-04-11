class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        sorted_dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))

        print(sorted_dic)
        #0:k까지 반환
        return list(sorted_dic.keys())[:k]