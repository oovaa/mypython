def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for i ,v in countries_dict.items():
        # Use a string method to format the required string.
        result += " ".join(v)+"\n"
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']

# s = "Hello how are you Contestant"
# k = 4
# h =s.split()
# h1 =""
# for i in range(k):
#     h1+=s.split()[i]+" "
# print(h1.rstrip)


# x = 0
# while True:
#   print(x:=x+1)

# class test:
#     x =0
#     def add(self,am : int)-> str:
#      self.x+=am
#      return self.x

# o = test()
# a = test()
# o.x=10

# print(type(o.add(11)))


# ff = open('romeo.txt').read()
# x =[i for i in ff if i != ' ' and i != '\n']
# print(max(x) , x.count(max(x)))
# # d = {(k,v) for (k,x.count(k)) in x}

# d = dict()
# for i in x:
#     d[i] =d.get(i,0)+1

# d = sorted(d.items())
# print(max(d))
# print(ord('y'))


# import time

# print(time.ctime(time.time())) #current time

# t= time.localtime()
# tt= time.strftime("%p %I:%M:%S ",t)
# print(tt)


# l1 = list(range(0,11))
# x = [x**2 for x in range(10)]
# x2 = [x**3 for x in range(10)]
# zz = zip(l1, x, x2)

# z = { x:z-y for (x,y,z) in zz }

# for i in z.items():
#  print(i,end=" ")


# a = dict([ ('brand', 1),  ('model', 3),(  'year',5)])
# print(a)

# a = list(filter(lambda x : x[0]!= 'year',a))
# print(a)


# print(a)
# a= list((map(lambda x : a[x]+1 ,a)))
# print((a))

# print(a)


# dct = {1: '1', 2 : '2'}
# print(dct)

# dct = dict(filter(lambda x : x[0] > 1, dct.items()))

# print(type(dct[2]))

# c = [1,3,5,6,8,9]

# def add(n):
#  return n+11


# print(c)

# c= list(map(add, c))
# print(c)


# a = {
#   'brand': 'Ford',test.py
#   'model': 'Mustang',
#   'year': 'Last year'
# }


# print(a)
# a=sorted(a.items(), key=lambda x: x[1][len(x[1])-2])
# print(a)

# print(bool('omer'[4:]))

# print('a' in ('a','v'))


# do = lambda x: x[len(x)-1]
# print(do('omer'))


# class duck:
#     def walk(self):
#      print('this duck is walking')

# class check:
#     def walk(self):
#      print('this check is walking')

# def ww(duck:duck):
#  duck.walk()

# o = duck()
# c = check()
# ww(c)#???


# class car:
#     color = None

# def chcolor(car,color):
#  car.color = color

# c1 = car()
# c2 = car()
# c3 = car()

# chcolor(c1,'red')
# chcolor(c2,'blue')
# chcolor(c3,'green')


# print(c1.color)
# print(c2.color)
# print(c3.color)


# from abc import ABC, abstractmethod


# class omer.(ABC):
#     @abstractmethod
#     def name(name, lastName='john'):
#         pass

#     def hah(self):
#      print('haha')

# class t(omer):
#     def name(name, lastName='john'):
#         print('hi',name,lastName)

# o = t()
# o.hah()


# class Person:
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age
#     def say_hi(self):
#         print('Hello, how are you?')


# class man(Person):
#     def __init__(self, name, age,gen):
#         Person.__init__(self, name, age)
#         self.gen = gen

#     def say_hi(self):
#         print('Hello, how are you?')


# m = man('omar',12,'mail')
# m.say_hi()

# class prey:
#   alive = True
#   def flee(self):
#    print('this animal flees ')

# class predetor():
#   def hunt(self):
#    print('this animal hunts')


# class fish(predetor,prey):
#   pass
# f = fish()
# f.flee()
# f.hunt()


# class car:
#   hh =55
#   def __init__(self, name, year):
#      self.name = name
#      self.year = year

#   def drive(self):
#    print('this',self.name,'is moving')

# c = car('bmw',2022)
# c.hh =1
# car.hh =44
# print(c.hh)

# #quiz game

# def newGame():
#  gusses = []
#  correct =0
#  qnum=1
#  for k in quts:
#    print(k)
#    for i in options[qnum-1]:
#      print(i)
#    gus = input('enter A , B , C , D : ').upper()
#    print(gus)
#    gusses.append(gus)
#    correct+= check(quts.get(k),gus)
#    qnum+=1
#  showScore(correct,gusses)

# def check(ans,gus)->int:
#   if ans == gus:
#     print('correct :)')
#     return 1
#   else:
#     print('Wrong :(')
#     return 0

# def showScore(correct,gusses):
#  print('answers :',end=' ')
#  for i in quts:
#   print(quts.get(i),end=' ')
#  print()

#  print('guesses :',end=' ')
#  for i in gusses:
#   print(i,end=' ')
#  print()

#  score = int(correct/len(quts)*100)
#  print('your score is', str(score)+'%')

# def playAgain():
#  res = input('wanna play again ? (y/n)').lower()
#  if res == 'y':
#    return True
#  else:
#    return False

# quts = {
#   'which one isthe predetor? ':'B',
#   'what is the worst uni ever?':'B',
#   'which number is the best?':'D',
#   'what is the actual name of the moon':'C',}

# options = (("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. UofK", "B. Sust", "C. Al-nilayn", "D. UofNY"),
#            ("A. 206", "B. 207", "C. 208", "D. 209"),
#            ("A. Mercury", "B. Venus", "C. omar", "D. Mars"))
# newGame()
# while playAgain():
#   newGame()
# print('\nByeeeee')


# class test:
#   def __init__(self, age):
#     self.age = age

#   def add(self)-> int:
#       return self.age+10

# omer = test(8)
# while expression:
#   if condition:
#     for item in range:
#         def name(args):
#           continue

# print(test.add(omer))


# def romanToInt(s: str) -> int:
#     val = {'I'        :     1,
# 'V'      :       5,
# 'X'       :      10,
# 'L'        :     50,
# 'C'         :    100,
# 'D'          :   500,
# 'M'           :  1000}
#     ans = 0
#     i=0
#     j=1
#     while j < len(s):
#       if val[s[j]]>val[s[i]]:
#           ans +=val[s[j]]-val[s[i]]
#           j+=2
#           i+=2
#       else:
#           ans +=val[s[i]]
#           i+=1
#           j+=1

#     return ans


# print(romanToInt("III"))

# import shutil
# shutil.copy2('romeo.txt','tata.txt')

# ff = open('romeo.txt','a')
# ff.write('yyyyooooo\nim ommmmer')

# import os
# path = '//home//omar//pyp//bank.py'
# if os.path.isdir(path):
#   print('it is here')
# else:
#     print('it is not here')


# import random as r
# ls = ['sci','paper']


# print("omer {o} nana {n}".format(o='man',n='maman'))

# def add(a:int,c:int)->any:
#  d = 20
#  return a+c

# print(add('8','5'))

# td = dict()
# td.update({'omer':19})
# td.update({'nana':18})
# td.update({'tata':15})
# print(td)
# td.update({'omer':33})
# print(td.get('ss',0))

# ls = list(x+10 for x in td.values() if x>17)
# print(ls)


# class test:
#   def __init__(self, age):
#     self.age = age

#   def add(self)-> int:
#       return self.age+10

# omer = test(8)
# print(test.add(omer))


# def romanToInt(s: str) -> int:
#     val = {'I'        :     1,
# 'V'      :       5,
# 'X'       :      10,
# 'L'        :     50,
# 'C'         :    100,
# 'D'          :   500,
# 'M'           :  1000}
#     ans = 0
#     i=0
#     j=1
#     while j < len(s):
#       if val[s[j]]>val[s[i]]:
#           ans +=val[s[j]]-val[s[i]]
#           j+=2
#           i+=2
#       else:
#           ans +=val[s[i]]
#           i+9=1
#           j+=1

#     return ans


# print(romanToInt("III"))

# def add(a:int,c:int)->any:
#  d = 20
#  return a+c

# print(add('8','5'))

# td = dict()
# td.update({'omer':19})
# td.update({'nana':18})
# td.update({'tata':15})
# print(td)
# td.update({'omer':33})
# print(td.get('ss',0))

# ls = list(x+10 for x in td.values() if x>17)
# print(ls)


# class test:
#   def __init__(self, age):
#     self.age = age

#   def add(self)-> int:
#       return self.age+10

# omer = test(8)
# print(test.add(omer))


# def romanToInt(s: str) -> int:
#     val = {'I'        :     1,
# 'V'      :       5,
# 'X'       :      10,
# 'L'        :     50,
# 'C'         :    100,
# 'D'          :   500,
# 'M'           :  1000}
#     ans = 0
#     i=0
#     j=1
#     while j < len(s):
#       if val[s[j]]>val[s[i]]:
#           ans +=val[s[j]]-val[s[i]]
#           j+=2
#           i+=2
#       else:
#           ans +=val[s[i]]
#           i+9=1
#           j+=1

#     return ans


# print(romanToInt("III"))


# def isPalindrome(x: int) -> bool:
#   x = str(x)
#   l = len(x)-1
#   s = 0
#   while s < len(x)/2:
#     if x[s] != x[l]:
#       return False
#     s+=1
#     l-=1
#   return True
# print(isPalindrome(10))


# def twoSum(self, nums: list[int], target: int) -> list[int]:
#  i= 0
#  hold = []
#  while i < len(nums):
#     j=0
#     while j < len(nums):
#        if j != i and nums[i]+ nums[j] == target:
#          hold.append(i)
#          hold.append(j)
#          return hold
#        j+=1
#     i+=1

# ls = [3,2,4]
# t=6
# print(twoSum(4,ls,t))


# t=int(input('enter fb rank :'))
# a=b=0
# x=1
# for i in range(t):
#     a=b
#     b=x
#     x=a+b
#     print(x)


# import random
# import string

# chars = string.punctuation+string.digits+string.ascii_letters+" "
# ls = list(chars)
# key = ls.copy()

# random.shuffle(key)
# #encrept
# mes = input('enter a message :')
# inmes =""
# for l in mes:
#     ind = ls.index(l)
#     inmes += key[ind]

# print(inmes)

# #decrept
# inmes = input('enter a message :')
# mes =""
# for l in inmes:
#     ind = key.index(l)
#     mes += ls[ind]

# print(mes)


# fh = open('mbox-short.txt')
# dh = dict()
# for i in fh:
#     for li in i.split():
#        dh[li] = dh.get(li,0)+1

# mw , mc =None,None
# for k ,v in dh.items():
#     if mc is None or v > mc and k != "jan":
#         mc = v
#         mw= k
# print(mw,mc)

# val = sorted(dh.items(),key=lambda x : x[1], reverse=True)
# print(val[1])


# man = ['omer','ahmed','mama'[2],34]
# print(man)
# man.append('tata')
# print(man.append)
# print(man[3]+11)
