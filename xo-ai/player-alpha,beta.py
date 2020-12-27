
import math
class player:
    def __init__(self,let):
        self.let=let

        
    def minimaxi(self,borad,ismax,alpha,beta,d):
        score=borad.evale()
        
        if score !=None :
         
            return score,d
        
        if ismax:
            best=-1000
            for y in range(3):
                for x in range(3):
                    if borad.borad[y][x]=='':
                        borad.borad[y][x]='x'
                        s,d=self.minimaxi(borad,not ismax,alpha,beta,d+1)
                        borad.borad[y][x]=''
                        best=max(s,best)
                        alpha=max(best,alpha)
                        if beta <= alpha:
                            return best,d
            return best,d
        
        
        else:
            best=1000
            for y in range(3):
                for x in range(3):
                    if borad.borad[y][x]=='':
                        borad.borad[y][x]='o'
                        s,d=self.minimaxi(borad,not ismax,alpha,beta,d+1)
                        borad.borad[y][x]=''
                        best=min(s,best)
                        beta=min(best,beta)
                   
                        if beta <= alpha:
                            return best,d
            return best,d
                    
       
                 
    def best_move(self,borad):
  
        sco=[]
        dd=[]
        pp=[]
        alpha=-1000
        beta=1000

        for y in range(3):
            for x in range(3):
                if borad.borad[y][x]=='':
                
                    borad.borad[y][x]='x'
                    s,d=self.minimaxi(borad,False,alpha,beta,1)
           
                    alpha=s
                    sco.append(s)
                    dd.append(d)
                    pp.append((x,y))
                    borad.borad[y][x]=''
        return (sco,pp,dd)
   
               
            
        
        