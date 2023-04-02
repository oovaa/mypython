class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        top =-1
        flen = len(nums)
        
        for i in range(min(k,len(nums))):
            if flen==1:
                if k==1:return -1
                else: return (nums[0])
                
            top = max(top,nums[0])
            nums.remove(nums[0])
            print(top,i,nums) 
        try:
            return max(top,nums[0])
        except IndexError:
            return top

nums =[99,95,68,24,18]
# nums =[35,43,23,86,23,45,84,2,18,83,79,28,54,81,12,94,14,0,0,29,94,12,13,1,48,85,22,95,24,5,73,10,96,97,72,41,52,1,91,3,20,22,41,98,70,20,52,48,91,84,16,30,27,35,69,33,67,18,4,53,86,78,26,83,13,96,29,15,34,80,16,49]
k=69
t = Solution()
print(t.maximumTop(nums,k))



# k=15
# top =-1
# flen = len(nums)
# for i in range(min(k,len(nums))):
#     if flen==1:
#         if k==1:
#             print(-1)
#             break
         
#         else: 
#             print(nums[0])
#             break
        
#     top = max(top,nums[0])
#     nums.remove(nums[0])
#     print(top,i,nums) 
# print(max(top,nums[0]))
 

      












# from datetime import datetime
# class Solution:
#     def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
#         s=0
#         for i in timeSeries:
#             if  i> s:
#                 s+=i+duration-1
#             elif i <=s:
#                 print(s)
#                 s=i+duration-s
#         return s

        
 
        
        
# start_time = datetime.now()
# s = Solution()
# print(s.findPoisonedDuration([1,4],2))
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))


# ls =[1,4]
# d =5
# s=0


# for i in ls:
#     if  i> s:
#        s+=i+d-1
#     elif i <=s:
#         print(s)
#         s=i+d-1
         
# print(s)
    



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


