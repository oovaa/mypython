import random
import string
 
chars = string.punctuation+string.digits+string.ascii_letters+" "
ls = list(chars)
key = ls.copy()

random.shuffle(key)
#encrept
mes = input('enter a message :')
inmes =""
for l in mes:
    ind = ls.index(l)
    inmes += key[ind]
 
print(inmes)

#decrept
inmes = input('enter a message :')
mes =""
for l in inmes:
    ind = key.index(l)
    mes += ls[ind]
 
print(mes)







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
