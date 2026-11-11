class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1


        for i in range(len(nums)):
            for j in range(len(nums)-1 , -1 , -1):
                if nums[i]+nums[j] == target and i !=j :
                    return [i,j]

