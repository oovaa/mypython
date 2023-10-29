# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



def maxProfit(prices):
    if len(prices) < 2:
        return 0

    n = len(prices)

    # Initialize the arrays
    buy = [0] * n
    sell = [0] * n
    cooldown = [0] * n

    # Base case
    buy[0] = -prices[0]

    # Fill in the arrays
    for i in range(1, n):
        cooldown[i] = max(cooldown[i - 1], sell[i - 1])
        buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i])
        sell[i] = buy[i - 1] + prices[i]

    # The maximum profit is the maximum of the last day's sell and cooldown
    return max(sell[n - 1], cooldown[n - 1])

# Example usage
prices1 = [1, 2, 3, 0, 2]
print(maxProfit(prices1))  # Output: 3

prices2 = [1]
print(maxProfit(prices2))  # Output: 0


# def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
#     return list(set(nums1).intersection(set(nums2)))


# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

# print(intersection(nums1, nums2))


# def isPowerOfThree(n: int) -> bool:
#     i = 1
#     if n == 1:
#         return True

#     while i < n / 2:
#         if 3**i == n:
#             return True
#         elif 3**i > n:
#             return False
#         i += 1


# print(isPowerOfThree(1))


# def isThree(n: int) -> bool:
#     divs = 1
#     for i in range(2, n + 1):
#         if n % i == 0:
#             divs += 1
#     return divs == 3

# print(isThree(9))


# def mag(n: int):
#     for i in range(n):
#         if i % 7 == 0:
#             yield i

# l = list(mag(199))

# print(l)


# from operator import itemgetter


# full = input("enter: ")
# full = full.split(" ")

# l = [tuple(x.split(",")) for x in full]

# print(sorted(l, key=itemgetter(0,1,2)))

# print(sorted(l, key=itemgetter(0, 1, 2)))

# print(l)


# from re import *

# value = []
# items = [x for x in input().split(",")]
# for p in items:
#     if len(p) < 6 or len(p) > 12:
#         continue
#     else:
#         pass
#     if not search("[a-z]", p):
#         continue
#     elif not search("[0-9]", p):
#         continue
#     elif not search("[A-Z]", p):
#         continue
#     elif not search("[$#@]", p):
#         continue
#     elif search("\s", p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))


# paswd = input("enter passwd: ")

# lowe = 0
# upper = 0
# digit = 0
# hash = 0

# if len(paswd) > 12 or len(paswd) < 6:
#     exit("invalid lenguth 6-12")

# for i, v in enumerate(paswd):
#     if v.isdigit():
#         digit += 1
#     elif v.isupper():
#         upper += 1
#     elif v.islower():
#         lowe += 1
#     elif v in "@#$":
#         hash += 1

# if lowe != 0 and upper != 0 and digit != 0 and hash != 0:
#     print("valid:", paswd)
#     exit(0)
# else:
#     print("invalid:", paswd)
#     exit(0)


# fullin = input("enter: ")

# sin = fullin.split(" ")

# sin = sin[:-1]
# # sin.pop() the same

# print(sin)
# amount = 0

# for i, v in enumerate(sin):
#     if v == "D":
#         amount += int(sin[i + 1])
#     elif v == "W":
#         amount -= int(sin[i + 1])

# print(amount)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ns = [x**2 if x %2 != 0 else x for x in range(0, 101)]
# print(ns)

# exlpain
# Take input as a single digit
# a = input("Enter a single digit: ")

# # Use the given formula to compute the result
# result = int(a) + int(a*2) + int(a*3) + int(a*4)
# print(result)


# s = input()
# d = dict()

# for c in s:
#     if c.isupper():
#         d["UPPER CASE"] = d.get("UPPER CASE", 0) + 1
#     elif c.islower():
#         d["LOWER CASE"] = d.get("LOWER CASE", 0) + 1
#     else:
#         pass
# print("UPPER CASE", d["UPPER CASE"])
# print("LOWER CASE", d["LOWER CASE"])

# stat = input("enter statment: ")

# c = 0
# l = 0

# for i in stat:
#     if i.isupper():
#         c += 1
#     if i.islower():
#         l += 1

# print(c, l)


# stat = input("enter words: ")

# d, l = 0, 0

# for i in stat:
#     if i.isdigit():
#         d += 1
#     elif i.isalpha():
#         l += 1
# print("LETTERS", d, "DIGITS", l)


# def checkeven(n: int):
#     if n == 0:
#         return 1

#     if n % 2 == 0:
#         return checkeven(n // 10)  # Return the result of the recursive call
#     else:
#         return 0

# # print(checkeven(246))

# for i in range(0, 10000):
#     if checkeven(i):
#         print(i)


# num = input("enter 4 didgts num: ")
# num = num.split(",")

# sum = 0

# for i in num:
#     i = int(i, 2)
#     if i % 5 == 0:
#         print(i)
#     sum += i
#     print(sum)


# p = 111
# print(int(str(p), 2))


# w = input("enter words: ")

# s = ""
# w =sorted( w.split(" "))

# for i in (w):
# 	if i not in s:
# 		s += " " + i
# s = s.lstrip()

# print(s)


# lines = []

# print("hit enter to break")

# while True:
#     lin = input()

#     if not lin:
#         break
#     lines.append(lin.upper())

# print("\n".join(lines))


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
