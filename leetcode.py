class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        pass
    
    
t = Solution()
s = "axxxxyyyyb"
part = "xy"
l = len(part)


while part in s:
    x = ''
    p = s.find(part)
    x = s[:p]+s[p+l:]

    print(s)
    s=x


print(s)
