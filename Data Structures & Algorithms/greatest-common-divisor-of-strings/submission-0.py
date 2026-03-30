class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        a = len(str1)
        b = len(str2)
        
        while b != 0:
            temp = b
            b = a % b
            a = temp
        
        result = ""
        for i in range(a):
            result += str1[i]
        
        return result

        