import random
wins = 0
loses = 0
while True:
    choice = ['rock','paper','scissors']
    com = random.choice(choice)
    ply = None
    while ply not in choice:
     ply = input("'rock','paper','scissors' :").lower()

    if ply == com:
        print("computer :",com)
        print("plyer :",ply)
        print('TIE!')
    elif ply == 'rock':
        if com == 'scissors':
                print("computer :",com)
                print("plyer :",ply)
                print('you win !!' )
                wins+=1
        elif com == 'paper':
                print("computer :",com)
                print("plyer :",ply)
                print('you lose :( ' )
                loses+=1
    elif ply == 'paper':
        if com == 'rock':
                print("computer :",com)
                print("plyer :",ply)
                print('you win !!' )
                wins+=1
                
        elif com == 'scissors':
                print("computer :",com)
                print("plyer :",ply)
                print('you lose :( ' )
                loses+=1
                
    elif ply == 'scissors':
        if com == 'paper':
                print("computer :",com)
                print("plyer :",ply)
                print('you win !!' )
                wins+=1
                
        elif com == 'rock':
                print("computer :",com)
                print("plyer :",ply)
                print('you lose :( ' )
                loses+=1
    wannaply= input("wanna ply again (y/n):")
    if wannaply != 'y':
      break
  
print('u won ',wins,'times :)')
print('u lost ',loses,'times :(')
print('thanks for playing with me :*')


