class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1=0
        ptr2=len(s)-1
        s=s.casefold()
        for i in range(len(s)//2):
            while not s[ptr1].isalnum():
                if ptr1==len(s)-1:
                    return True
                ptr1+=1
            while not s[ptr2].isalnum():
                if ptr2==0:
                    return True
                ptr2-=1
            if s[ptr1]!=s[ptr2]:
                return False
            ptr1+=1
            ptr2-=1
        return True