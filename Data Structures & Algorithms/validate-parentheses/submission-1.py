class Solution:
    def isValid(self, s: str) -> bool:
        st=list()
        dic={")":"(","}":"{","]":"["}
        for char in s:
            if char in dic:
                if st and st[-1]==dic[char]:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)
        return True if len(st)==0 else False
        
        