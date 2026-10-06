class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S=0
        D={}
        S_max_seen=0
        left=0
        for right in range (len(s)):
            
            if s[right] in D:
                while s[right] in D:
                    D.pop(s[left])
                    left += 1
                    S -= 1
            if s[right] not in D:
                D[s[right]]=1
                S+=1
            if S>S_max_seen:
                S_max_seen=S
        return S_max_seen

                

        
        