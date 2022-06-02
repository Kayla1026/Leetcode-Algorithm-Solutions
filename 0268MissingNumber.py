#My solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_lst=[i for i in range(len(nums)+1)]
        return list(set(full_lst).difference(set(nums)))[0]

#Math Solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_value=int(max(nums))
        true_len=max_value+1
        return int((max_value)*true_len/2-sum(nums))




 


 



 
  
    
