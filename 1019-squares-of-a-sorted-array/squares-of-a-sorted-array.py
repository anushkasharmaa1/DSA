class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a_pos=[]
        b_neg=[]
        for i in range (len(nums)):
            if nums[i]>=0:
                a_pos.append(nums[i])
            else:
                b_neg.append(nums[i])
        
        if len(b_neg)==0:
            for i in range(len(nums)):
                nums[i]=nums[i]*nums[i]
            return nums
        
        if len(a_pos)==0:
            for i in range(len(nums)):
                nums[i]=nums[i]*nums[i]
            nums.reverse()
            return nums

        for i in range(len(a_pos)):
            a_pos[i]=a_pos[i]*a_pos[i]
        
        for i in range(len(b_neg)):
            b_neg[i]=b_neg[i]*b_neg[i]
        b_neg.reverse()
        
        result = []
        i = 0
        j = 0
        
        while i < len(a_pos) and j < len(b_neg):
            if a_pos[i] < b_neg[j]:
                result.append(a_pos[i])
                i += 1
            else:
                result.append(b_neg[j])
                j += 1
        
        while i < len(a_pos):
            result.append(a_pos[i])
            i += 1
        
        while j < len(b_neg):
            result.append(b_neg[j])
            j += 1
            
        return result


        
        

        
        
        

        