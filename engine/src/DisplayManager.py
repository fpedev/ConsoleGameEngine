import os


class Display():
    def __init__(self, rows, columns, fill):
        self.rows = rows
        self.columns = columns
        self.fill = fill

        if self.fill == None: self.fill = " "

        self.screen = []

        for x in range(rows):
            self.screen.append([])
            for _ in range(columns):
                self.screen[x].append(self.fill) 

    def render(self):
        toRender = ""
        for rows in range(len(self.screen)):
            if rows != 0:
                toRender = toRender + "\n"
            for columns in range(len(self.screen[rows])):
               toRender = toRender + str(self.screen[rows][columns])
        print(toRender)

    def clear(self): 
        os.system('cls')
        self.screen.clear()
        for x in range(self.rows):
            self.screen.append([])
            for _ in range(self.columns):
                self.screen[x].append(self.fill) 

    def setPos(self, x, y, value):
        self.screen[y-1][x-1] = value

    def isInside(self, x, y):
        return self.columns >= x and self.rows >= y


def create(rows, size, fill):
   return Display(rows,size,fill)
