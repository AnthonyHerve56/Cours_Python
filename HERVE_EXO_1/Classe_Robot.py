class Robot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def Monter(self):
        self.y-=1
        if self.y<0:
            self.y=0
    def Descendre(self):
        self.y+=1
        
    def Aller_a_gauche(self):
        self.x-=1
        if self.x<0:
            self.x=0
    def Aller_a_droite(self):
        self.x+=1
        
    def Position_du_Robot(self):
        print(f"Position en x {self.x} et Position en y {self.y}")
    
    def Reinitialise_position(self):
        self.x=0
        self.y=0