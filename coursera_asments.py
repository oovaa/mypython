# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
c = int(input('Enter count: '))
p = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
  if 'Fikret ' in tag:
    print(tag.get('href', None))








# # To run this, download the BeautifulSoup zip file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup('span')
# c=0
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#     c+=int(tag.contents[0])
# print(c)





# import math
# from turtle import *
# def hearta(k):
#   return 15*math.sin(k)**3

# def heartb(k):
#   return 12*math.cos(k)-5*\
#     math.cos(2*k)-2*\
#       math.cos(3*k)-\
#         math.cos(4*k)
# speed(500)
# bgcolor('black')
# for i in range(10000):
#   goto(hearta(i)*20,heartb(i)*20)
#   for j in range(5):
#     color("#f73487")
#   goto(0,0)
# done()
   
 



# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
    
# mysock.close()





# In this assignment you will read through and parse a
# file with text and numbers. You will extract all the
# numbers in the file and compute the sum of the numbers.
# import re

# f= open('regexft.txt')
# h1= []
# for i in f:
#   h = re.findall('[0-9]+',i)
#   h1.extend(h)
  
# sh =0
# for i in h1:
#   sh += int(i)

# print(sh)

# print(sum([ i for i  in f'[0-9]+',**************************.read()) ] ) )

 

 



# s = " omer 12 in 2003 learning py3a"
# s1 = " omer 19 in 555 learning py8"

# h = re.findall('[0-9]+',s)
# h1 = re.findall('[0-9]+',s1)
# h1.extend(h)
# print(h1)








# 10.2 Write a program to read through the
# mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages.
# You can pull the hour out from the 'From '
# line by finding the time and then splitting 
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# count= 0
# dh = dict()
# for line in handle:
#   if line.startswith('From'):
#     count+=1
#     if count%2==1:
#       hold = line.split()[5].split(':')[0]
#       dh[hold] = dh.get(hold,0)+1
      
# dh =sorted(dh.items())
# for k,v in dh:
#   print(k,v)
  
     
 

# 9.4 Write a program to read through the mbox-short.
# txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in 
# the file. After the dictionary is produced, the program 
# reads through the dictionary using a maximum loop to find 
# the most prolific committer.

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# emaild = dict()
# for line in handle:
#   if line.startswith('From'):
#     emaild[line.split()[1]] = emaild.get(line.split()[1],0)+1
# sed = sorted(emaild.items(), key=lambda x : x[1], reverse=True) #cool asf
# print(sed[0][0],int(sed[0][1]/2))
    



# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word
# in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the count.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# hell yeah i fixed it
# fh = open(fname)
# count = 0
# cn2 =0
# for i in fh:
#   if not i.startswith('From'):
#     continue
 
#   cn2+=1
#   if cn2%2==0:
#    continue
 
#   print(i.rstrip().split()[1])
#   count+=1

# print("There were", count, "lines in the file with From as the first word")






# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split()
# method. The program should build a list of words.
# For each word on each line check to see if the word is 
# already in the list and if not append it to the list.
# When the program completes, sort and print the resulting 
# words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#  l = line.split()
#  for i in l:
#    if i not in lst:
#      lst.append(i)
# lst.sort()
# print(lst)

 

# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from
# each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum()
# function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# count =0
# hold =0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     hold+=float(line[line.find("0"):])
#     count+=1
# print('Average spam confidence:',hold/count)



# 7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file, 
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

# Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for i in fh:
#      print(i.upper().rstrip())


# 6.5 largest = None
# smallest = None
# while True:
#     num = (input("Enter a number: "))
#     if num == "done":
#         break  
#     try:
#      num= int(num)   
#     except:
#       print('Invalid input')
#       continue
#     if largest is None:
#      largest = num
#     elif largest < num:
#      largest =num   
#     if smallest is None:
#       smallest = num
#     elif smallest >num:
#       smallest = num

     
# print("Maximum is", int(largest))
# print("Minimum is",  int(smallest))



# 4.6 def computepay(h, r):
#     if h > 40:
#       hold = h - 40
#       return 40*r + hold*r*1.5
#     else:
#       return h*r
# hrs = float(input("Enter Hours:"))
# rate =float( input("Enter rate:"))
# p = computepay(hrs, rate)

# print("Pay", p)


# 3.3 score = float(input("Enter Score: "))
# if score >= 0.9 and score <= 1.0:
#   print('A')
# elif score >= 0.8 and score <= 1.0 :
#   print('B')
# elif score >= 0.7 and score <= 1.0:
#   print('C')
# elif score >= 0.6 and score <= 1.0:
#   print('D')
# elif score < 0.6 and score <= 1.0:
#   print('F')
# else:
#   print('Error')
#   quit()


# 6.5  Write code using find() and string slicing (see section 6.10) to
#   extract the number at the end of the line below. Convert the extracted 
#   value to a floating point number and print it out.
# text = "X-DSPAM-Confidence:    0.8475"
# print(float(text[text.find("0"):]))

  
  # 3.1 Write a program to prompt the user for hours 
  # and rate per hour using input to compute gross pay.
  # Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
  # Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
  # You should use input to read a string and float() to convert the string to a number.
  # Do not worry about error checking the user input -
  # assume the user types numbers properly.
# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter rate:")
# r = float(rate)
# if h > 40:
#   hold =h-40
#   print(40*r+hold*r*1.5)
# else:
#   print(r*h)