palance = 5000
while True:
     op = input('A.show palance \nB.take money \nD.store money\nE.end:').upper()
     if op =='A':
       print(palance)
     elif op == 'B':    
         amount = int(input('Enter amount of cash :'))
         if amount > palance:
             print('u dont have that much money')
             continue
         palance -= amount
         print('u have ',palance,'left')
     elif op == 'D':
         amount = int(input('Enter amount of cash :'))
         palance += amount
         print('u have ',palance,'left')
     elif op =='E':
       break

