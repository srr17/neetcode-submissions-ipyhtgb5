class Solution:
    def isHappy(self, n: int) -> bool:
        l1=[]
        while n!=1:
            if n in l1:
                return False
            l1.append(n)
            c=0
            while n>0:
                c=(n%10)**2+c
                n=n//10
            n=c
        return True

        