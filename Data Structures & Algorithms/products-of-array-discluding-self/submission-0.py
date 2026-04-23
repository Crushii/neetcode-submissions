from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [reduce(lambda x , y : x*y,list(nums[:i]+nums[i+1:])) for i in range(0,len(nums))]
        