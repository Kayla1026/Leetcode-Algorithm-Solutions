#Two Sum
#Complex solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1:
            if nums[0]==target:
                return [0]
        elif len(nums)==2:
            if nums[0]+nums[1]==target:
                return [0,1]
        else:
            result=[]
            for i in range(len(nums)):
                start=i+1
                end=len(nums)
                for e in range(start,end):
                    sum=nums[i]+nums[e]
                    if sum==target:
                        result.append(i)
                        result.append(e)
                        return result

#Other solution: Hashtable from https://leetcode.com/problems/two-sum/discuss/311515/Python-Hash_Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i
