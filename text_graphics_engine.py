#graphics_engine.py

import os

class screen:
    def __init__(self,size,blank):
        self.size,self.blank = size,blank
        self.coords = []
        self.objs = []
        self.draw_screen()
        for i in range(self.size[1]+1):
            self.coords.append([])
            for e in range(self.size[0]+1):
                self.coords[len(self.coords)-1].append(coord([e,i],self.blank,[255,255,255]))
    def draw_screen(self):
        for i in self.objs:
            i.update()
        for i in self.coords:
            for e in i:
                print(e.type_coord,end="")
            print("")
    def clear_screen(self,debug=[]):
        os.system('cls' if os.name=='nt' else 'clear')
        self.draw_screen()
        for i in debug:
            print(i)
    def find_coord(self,coord):
        answer = None
        for i in self.coords:
            for e in i:
                if e.pos == coord:
                    answer = e
                    break
        if not answer == None:
            return answer
        else:
            raise ValueError ("COORDINATE OUT OF RANGE")
            

class coord:
    def __init__(self,pos,type_coord,color):
        self.pos,self.type_coord,self.color = pos,type_coord,color

class obj:
    def __init__(self,coords,type_coord,color,screen):
        self.coords,self.type_coord,self.color,self.screen = coords,type_coord,color,screen
        self.update()
        self.screen.objs.append(self)
        
    def update(self):
        for i in self.coords:
            try:
                self.screen.find_coord([round(i[0]),round(i[1])]).type_coord = self.type_coord
            except:
                pass
        
    def clear(self):
        for i in self.coords:
            try:
                self.screen.find_coord([round(i[0]),round(i[1])]).type_coord = self.screen.blank
            except:
                pass
    
    def set_coords(self,coords):
        self.clear()
        self.coords = coords
        self.update()
    
    def __add__(self,pos):
        self.clear()
        for i in self.coords:
            i[0] += pos[0]
            i[1] += pos[1]
        self.update()
    
    def __eq__(self,obj2):
        touching = False
        for i in obj2.coords:
            for e in self.coords:
                if [round(i[0]),round(i[1])] == [round(e[0]),round(e[1])]:
                    touching = True
                    break
        self.clear()
        self.update()
        return touching

# now, to clear the screen
if __name__ == "__main__":
    print("Don't run me, I'm a library")
    
