from datetime import datetime
class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        s=0
        for i in timeSeries:
            if  i> s:
                s+=i+duration-1
            elif i <=s:
                print(s)
                s=i+duration-s
        return s

        
 
        
        
# start_time = datetime.now()
s = Solution()
# print(s.findPoisonedDuration([1,4],2))
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))


ls =[1,4]
d =5
s=0


for i in ls:
    if  i> s:
       s+=i+d-1
    elif i <=s:
        print(s)
        s=i+d-1
        
        
    

         
print(s)
    

        
 



# a = [3,4]
# a.append(6)

# print(a)


    
# x= [1,1,4,6,8,8,8,4,2]
# print(len(set(x)))
# print(list(dict.fromkeys(x)))







# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         pass
    
    
# t = Solution()
# s = "axxxxyyyyb"
# part = "xy"
# l = len(part)


# while part in s:
#     x = ''
#     p = s.find(part)
#     x = s[:p]+s[p+l:]

#     print(s)
#     s=x

# print(s)


