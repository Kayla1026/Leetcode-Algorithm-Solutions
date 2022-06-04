#My solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res={}
        for i in nums:
            res[i]=res.get(i,0)+1
        stan=len(nums)/2
        return [k for k,v in res.items() if v > stan][0]