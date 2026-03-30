class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        test=list(s)
        for i in t:
            if i in test:
                test.remove(i)
            else:
                return False
        return True
        