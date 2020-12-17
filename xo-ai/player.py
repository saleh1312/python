
import math
class player:
    def __init__(self,let):
        self.let=let
        

    def minimaxi(self,borad,depth,ismax=True):
        depth=depth
        score=borad.evale()
        
        if score !=None :
            return score,depth
        
     
        sco=[]
        
        for y in range(3):
            for x in range(3):
                if borad.borad[y][x]=='':
                    if ismax:
                        
                        borad.borad[y][x]='x'
                    else:
                        borad.borad[y][x]='o'
                    s,d=self.minimaxi(borad,depth+1,not ismax)
                    depth=d
                    sco.append(s)
                    borad.borad[y][x]=''
                    
        return (max(sco) if ismax else min(sco)),depth
                 
    def best_move(self,borad):
  
        sco=[]
        dd=[]
        pp=[]
        for y in range(3):
            for x in range(3):
                if borad.borad[y][x]=='':
                    
                    borad.borad[y][x]='x'
                    s,d=self.minimaxi(borad,1,False)
                    sco.append(s)
                    dd.append(d)
                    pp.append((x,y))
                    borad.borad[y][x]=''
        return (sco,dd,pp)
   
               
            
        
        