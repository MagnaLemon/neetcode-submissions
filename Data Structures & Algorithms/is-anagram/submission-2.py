class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        for i in s:
            a.append(i)
        a.sort()
        
        b=[]
        for i in t:
            b.append(i)
        b.sort()
        if a==b:
            return True
        else:
            return False