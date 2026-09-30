class Solution:
    def scoreOfString(self, s: str) -> int:
        n1 = 0
        n2 = 0
        for i in range(len(s)-1):
            n1 = abs(ord(s[i])-ord(s[i+1]))
            n2 += n1
        return n2