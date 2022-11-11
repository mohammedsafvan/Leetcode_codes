class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if dic.keys().__contains__(i):
                dic[i] = dic.get(i) + 1
            else:
                dic[i] = 1
        
        for k,v in dic.items():
            if v==1:
                return k