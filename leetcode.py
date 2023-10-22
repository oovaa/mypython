

# words = input("enter words ").split(",")
# words.sort()
# print(" | ".join(words).split("|"))


# strin = input("enter num ").split(",")
# x = int(strin[0])
# y = int(strin[1])

# arr = []

# for i in range(1, x + 1):
#     inerarr = []
#     for j in range(1, y + 1):
#         inerarr.append(i * j)
#     arr.append(inerarr)

# print(arr)


# from math import sqrt

# c = 50
# h = 30
# d = input("enter d plz: ")

# ins = d.split(",")

# for i in range(len(ins)):
#     q = int(sqrt((2 * c * int(ins[i])) / h))
#     ins[i] = str(q)

# print(','.join(ins))


# class man:
#     s = ""
#     def getString(self):
#         self.s = input("enter something: ")


#     def printString(self):
#         if " " in  self.s:
#             self.s= self.s[:self.s.index(" ")]
#         print(self.s.upper())

# mna = man()
# mna.getString()
# mna.printString()

# values = input("enter values: ")

# ll = values.split(",")
# tt = tuple(ll)

# print(ll)
# print(tt)

# command = "(al)G(al)()()G"
# print(command :=command.replace('()', 'o'))
# print(command:= command.replace("(",""))
# print(command :=command.replace(")",""))


# grid = [[9,81],[33,17]]


# ans =0
# mh =0
# for i in grid:
#   h = max(i)
#   i.remove(h)
#   mh = max(h,mh)
#   ans+=mh
#   print(h,mh,ans)
# print(ans)


# nums = [1,2,3,4,5]
# # ans = (sum([x for x in nums if nums.count(x)==1]))
# ans = 0
# for i in nums:
#   if nums.count(i)>1:
#     continue
#   ans+=i
# # return ans


# print(ans)


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if set(list(s))!=set((list(t))):
#           return False
#         hold = dict()
#         for i in enumerate(s):
#             if hold.get(i[1]) is None: hold[i[1]] = t[i[0]]
#         for i in enumerate(s):
#             # print(hold[i[1]],t[i[0]])
#             if hold[i[1]] != t[i[0]]:
#               return False
#         return True


# ans = True
# s = "badc"
# t = "baba"
# # t1= Solution()
# # print(t1.isIsomorphic(s,t))

# # s = "egg"
# # t = "add"


# map1 = []
# map2 = []
# for idx in s:
#     map1.append(s.index(idx))
#     print(s.index(idx),idx,end=" ")
# print()

# for idx in t:
#     map2.append(t.index(idx))
#     print(t.index(idx),idx,end=" ")
# print()
# print(map1)
# print(map2)

# print(z:=set(zip(s,t)))

# ans = [x[0] for x in z]
# print((ans))


# for i in enumerate(s):
#     print(hold[i[1]],t[i[0]])
#     if hold[i[1]] != t[i[0]]:
#       print('False')
#       break
#     print('True')


# class Solution:
#     def maximumTop(self, nums: list[int], k: int) -> int:
#         top =-1
#         flen = len(nums)

#         for i in range(min(k-1,len(nums))):
#             if flen==1:
#                 if k==1:return -1
#                 else: return (nums[0])

#             top = max(top,nums[0])
#             nums.remove(nums[0])
#             print(top,i,nums)
#         try:
#             return max(top,nums[0])
#         except IndexError:
#             return top

# # nums =[35,43,23,86,23,45,84,2,18,83,79,28,54,81,12,94,14,0,0,29,94,12,13,1,48,85,22,95,24,5,73,10,96,97,72,41,52,1,91,3,20,22,41,98,70,20,52,48,91,84,16,30,27,35,69,33,67,18,4,53,86,78,26,83,13,96,29,15,34,80,16,49]
# nums =[91,98,17,79,15,55,47,86,4,5,17,79,68,60,60,31,72,85,25,77,8,78,40,96,76,69,95,2,42,87,48,72,45,25,40,60,21,91,32,79,2,87,80,97,82,94,69,43,18,19,21,36,44,81,99]
# k=2
# t = Solution()
# print(t.maximumTop(nums,k))


# k=2
# top =-1
# flen = len(nums)

# for i in range(min(k-1,len(nums))):
#     maxi =-1
#     if (len(nums) == 1) and (k & 1):
#         print(-1)
#         break

#     maxi = max(maxi, nums[i])

# if k < len(nums):
#     maxi = max(maxi, nums[k])
# print(maxi)


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
