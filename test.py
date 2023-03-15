
#quiz game

def newGame():
 gusses = []
 correct =0
 qnum=1
 for k in quts:
   print(k)
   for i in options[qnum-1]:
     print(i)
   gus = input('enter A , B , C , D : ').upper()
   gusses.append(gus)
   correct+= check(quts.get(k),gus)
   qnum+=1
 showScore(correct,gusses)
   

def check(ans,gus)->int:
  if ans == gus:
    print('correct :)')
    return 1
  else:
    print('Wrong :(')
    return 0
    
    
 
def showScore(correct,gusses):
 print('answers :',end=' ')
 for i in quts:
  print(quts.get(i),end=' ')
 print()
 
 print('guesses :',end=' ')
 for i in gusses:
  print(gusses[i],end=' ')
 print()
 
 score = int(correct/len(quts)*100)
 print('your score is', str(score)+'%')
 
 
  
def playAgain(args):
 pass

quts = {
  'which one isthe predetor? ':'B',
  'what is the worst uni ever?':'C',
  'which number is the best?':'D',
  'what is the actual name of the moon':'C',}

options = (("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. UofK", "B. Sust", "C. Al-nilayn", "D. UofNY"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. omar", "D. Mars"))
newGame()



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
#print(ls)
   
 
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
#print(ls)
   
 
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
