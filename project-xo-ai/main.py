from clases import borad
from player import player
from player2 import player as player2
import math



c='o'
p='x'
human=player(p)
com=player(c)
com2=player2(c)


bord = borad(c,p)

bord.show()

print('player='+p+'  com='+c)
while 1:
 
  
    x=input('inter x')
    y=input('inter y')
    w=bord.change(human,(int(x),int(y)))
    
    if w is not None:
        if w==1:
            print('conputer won')
        elif w==-1:
        
            print('player won')
        elif w==2:
            continue
        else:
            print('tie')
        break
    
    
    
    (s,pp,dd)=com.best_move(bord)
    (s2,pp2,dd2)=com2.best_move(bord)
    
    big_score=-1000

    index=0
    for i in range(len(s)):
        if s[i]>big_score:
            big_score=s[i]
            index=i
            
            
    print('\n\n')
    print('============================')
    print('minimax information without alpha betta :')
    
    
    print(s2)
    print(dd2)
    
    print('========================')
    
    print('minimax information with alpha betta :')
    
    
    print(s)
    print(dd)
    print('============================')
    
            
            
            
   
    w=bord.change(com,(pp[index][0],pp[index][1]))
    bord.show()
    if w is not None:
        if w==1:
            print('conputer won')
        elif w==-1:
        
            print('player won')
        else:
            print('tie')
        break
  
    
                