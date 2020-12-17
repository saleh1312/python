from clases import borad
from player import player
import math

bord = borad()

bord.show()

human=player('o')
com=player('x')


while 1:
    print('player=o  , com=x')
  
    x=input('inter x')
    y=input('inter y')
    bord.change(human,(int(x),int(y)))

    (s,d,pp)=com.best_move(bord)
    print(s)
    print(d)
    print(pp)
    
    ss=-math.inf
    d2=math.inf
    x2,y2=0,0
    
    ou=0
    for i in range(len(s)):
        if s[i]>ss:
            ss=s[i]
            d2=d[i]
            ou=i
        elif s[i]==ss:
            if d[i] <d2:
                ss=s[i]
                d2=d[i]
                ou=i
            
            
   
    bord.change(com,(pp[ou][0],pp[ou][1]))
  
    bord.show()
                