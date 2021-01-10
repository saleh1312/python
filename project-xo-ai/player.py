
import math
class player:
    def __init__(self,let):
        self.let=let
        if let=='x':
            
            self.com='x'
            self.player='o'
        else:
            self.com='o'
            self.player='x'
   

        
    def minimaxi(self,borad,ismax,alpha,beta,d):
        score=borad.evale()
        
        if score !=None :
         
            return score,d
        
        if ismax:
            best=-1000
            for y in range(3):
                for x in range(3):
                    if borad.borad[y][x]=='':
                        
                        borad.borad[y][x]=self.com
                        
                        s,d=self.minimaxi(borad,not ismax,alpha,beta,d+1)
                        
                        borad.borad[y][x]=''
                        if s > best:
                            best=s
                            
                        if best > alpha:
                            alpha = best
                 
                        if alpha >= beta:
                            return best,d
                        
                       
            return best,d
        
        
        else:
            best=1000
            for y in range(3):
                for x in range(3):
                    if borad.borad[y][x]=='':
                        borad.borad[y][x]=self.player
                        s,d=self.minimaxi(borad,not ismax,alpha,beta,d+1)
                        borad.borad[y][x]=''
                        
                        if s < best:
                            best=s
                            
                            
                        if best < beta:
                            beta = best
                 
                        if beta <= alpha:
                            return best,d
                        
                        
            return best,d
                    
       
                 
    def best_move(self,borad):
  
        scores=[]
        depths=[]
        points=[]
        
        alpha=-1000
        beta=1000

        for y in range(3):
            for x in range(3):
                if borad.borad[y][x]=='':
                
                    borad.borad[y][x]=self.com
                    s,d=self.minimaxi(borad,False,alpha,beta,1)
           
                    if alpha>s:
                        alpha=s
                        
                    scores.append(s)
                    depths.append(d)
                    points.append((x,y))
                    borad.borad[y][x]=''
                    
        return (scores,points,depths)
   
               
            
        
        