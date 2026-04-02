class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]
        i=0
        j=len(numbers)-1
        while(i<j):
            sum=numbers[i]+numbers[j]
            if (sum==target):
                result.append(i+1)
                result.append(j+1)
                return result
            elif (sum>target):
                j-=1
            else:
                i+=1
        return result
        
        