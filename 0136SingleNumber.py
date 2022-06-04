#My solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res={}
        for i in nums:
            res[i]=res.get(i,0)+1
        return [k for k, v in res.items() if v == 1][0]

#XOR https://leetcode.com/problems/single-number/discuss/558787/Python-3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        r=nums[0]
        for i in range(1,n):
            r = r ^ nums[i] 

        return r