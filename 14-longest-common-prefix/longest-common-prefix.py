class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]

        answer=""

        for i in range(len(first)):
            if i<len(last) and first[i]==last[i]:
                answer+=first[i]
            else:
                break
        return answer
        