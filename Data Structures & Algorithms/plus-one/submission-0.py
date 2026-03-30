class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        c=0
        for i in range(len(digits)):
            num=num*10+digits[i]
        num+=1
        lst = []

        while num > 0:
            lst.append(num % 10)
            num //= 10

        lst.reverse()
        return lst
        