class borad:
    def __init__(self,com,player):
        self.borad=[
            ['','',''],
            ['','',''],
            ['','',''],
            ]
        
        self.pp={com:1,player:-1}
        
    def show(self):
        print(self.borad[0])
        print(self.borad[1])
        print(self.borad[2])
        
        
    def change(self,player,pos):
        xc,yc=pos
        
        for x in range(0,3):
            for y in range(0,3):
                if x==xc and y==yc:
                    if self.borad[y][x]=='':
                        
                        self.borad[y][x]=player.let
                    else:
                        print('not valid try again ...')
                        return 2
        return self.evale()
                
                
    
        
        
    def clear(self):
        self.borad=[
            ['','',''],
            ['','',''],
            ['','',''],
            ]
        
        
        
    def evale(self):
        if self.borad[0][0]==self.borad[0][1]==self.borad[0][2] and self.borad[0][0]!='':
            pl=self.borad[0][0]
            return self.pp[pl]
            
        elif self.borad[1][0]==self.borad[1][1]==self.borad[1][2] and self.borad[1][2]!='':
            pl=self.borad[1][0]
            return self.pp[pl]
        
        elif self.borad[2][0]==self.borad[2][1]==self.borad[2][2] and self.borad[2][2]!='':
            pl=self.borad[2][0]
            return self.pp[pl]
        
        elif self.borad[0][0]==self.borad[1][0]==self.borad[2][0] and self.borad[2][0]!='':
            pl=self.borad[0][0]
            return self.pp[pl]
        
        elif self.borad[0][1]==self.borad[1][1]==self.borad[2][1] and self.borad[2][1]!='':
            pl=self.borad[0][1]
            return self.pp[pl]
        
        elif self.borad[0][2]==self.borad[1][2]==self.borad[2][2] and self.borad[2][2]!='':
            pl=self.borad[0][2]
            return self.pp[pl]
        
        elif self.borad[0][0]==self.borad[1][1]==self.borad[2][2] and self.borad[2][2]!='':
            pl=self.borad[0][0]
            return self.pp[pl]
        
        elif self.borad[2][0]==self.borad[1][1]==self.borad[0][2] and self.borad[0][2]!='':
            pl=self.borad[0][2]
            return self.pp[pl]
        
        
        
        else :
            #if tie
            
            
            lo=0
            for y in range(3):
                for x in range(3):
                    if self.borad[y][x]=='':
                        lo=1
            if lo==0:
                
                return 0
        
        
        
        
        