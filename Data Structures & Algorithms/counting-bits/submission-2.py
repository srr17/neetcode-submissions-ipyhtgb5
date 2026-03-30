class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            c=0
            num=i
            while num>0:
                c+=num%2
                num//=2
            ans.append(c)
        return ans
