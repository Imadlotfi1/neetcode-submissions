class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for word in strs:
            s+=str(len(word))+'#'+word
        return s

    
    def decode(self, s: str) -> List[str]:
        A=[]
        #but to decode i should look for diez then split from diez into the len the 
        # i will use the two pointers method 
        i,j=0,len(s)-1
        while i<len(s):
            j=i #j becomes i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            # so j+1 is diez because we have stopped at the last number which is j
            A.append(s[j+1:j+1+length])
            i=j+1+length
        return A
                





