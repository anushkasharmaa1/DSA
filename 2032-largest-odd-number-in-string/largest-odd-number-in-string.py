class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        j=-1
        for i in range(n-1, -1, -1):
            if int(num[i])%2!=0:
                j=i
                break
        if j==-1:
            return ""
        return num[0:j+1]

        