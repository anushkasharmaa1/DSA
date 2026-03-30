class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        size=len(nums)
        for i in range (0, size):
            for j in range(i+1, size):
                if(nums[i]+nums[j]== target):
                    result.append(i)
                    result.append(j)
                    return result
