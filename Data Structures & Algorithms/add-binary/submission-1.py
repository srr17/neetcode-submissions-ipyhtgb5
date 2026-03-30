class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i= len(a)-1
        j= len(b)-1
        result=''
        carry=0
        while carry or i>=0 or j>=0:
            num1=int(a[i]) if i>=0 else 0
            num2=int(b[j]) if j>=0 else 0
            total=num1+num2+carry
            result=str(total%2)+result
            carry=total//2
            i-=1
            j-=1
        return result
