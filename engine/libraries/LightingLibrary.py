class Light():
    def __init__(self, x,y,strength):
        self.x = x
        self.y = y
        self.strength = strength + 1
    def draw(self,display):
        for strength in range(self.strength):
            if strength == 0:
                display.setPos(self.x,self.y, "x")
            else:
                for i in range(strength):
                    display.setPos((self.x + i) + 1,self.y, (strength - i))
                    display.setPos((self.x - i) - 1,self.y, (strength - i))

                    display.setPos(self.x,(self.y - i) - 1, (strength - i))
                    display.setPos(self.x,(self.y + i) + 1, (strength - i))