from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController

__ =False

app = Ursina()





class Player(FirstPersonController):
     def __init__(self):
          super().__init__(
               speed = 10,
               model = 'cube',
               collider = 'mesh',
               scale = 1,
               jump_height=0
            )
          

player = Player()
#EditorCamera()


class EXIT(Entity):
     def __init__(self,i,j):
          super().__init__(
               model='cube',
               scale=(5,5,5),
               color=color.black,
               position=(i*5,0,j*5,),
               collider='box'
          )
          self.player=player
          self.text=Text(
               text='team difference!// GG',
               scale=2,
               origin=(0.0),
               visible=False
          )
     def update(self):
         self.clear()     
     def clear(self):
        dis = (self.player.position-self.position).length()
        print(dis)
        if dis<3:
             self.player.enabled=False
             self.text.visible=True
     
          

def input(key):
     if key == 'escape':
          app.quit()
     


MAP =[
     [11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,__,__,__,34,11,22,33,44,55,66,77,88,99,99,56,45,34,__,__,__,__,__,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,__,__,__,__,__,__,__,__,__,65,__,__,__,65,24,77,21,43,12,23,12,63,__,34,__,34,__,__,__,44,55,66,77,88,99,99,56,45,34,__,23,__,65,__,__,__,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,__,66,77,88,__,99,56,45,34,34,23,__,65,24,77,21,43,12,__,__,__,__,34,__,__,__,22,__,__,55,66,77,88,99,99,56,45,__,__,23,__,65,__,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,__,66,77,88,'p',__,45,45,34,34,23,__,__,__,77,21,43,12,__,12,63,45,34,34,34,11,22,__,44,55,66,77,88,99,99,56,45,__,34,23,45,__,__,77,21,43,12,23,12,63,45,__,34,34],
     [11,22,33,44,__,66,77,88,__,99,56,45,34,34,23,__,65,__,__,21,43,12,__,12,63,45,34,34,34,11,__,__,__,55,66,77,88,99,99,56,45,__,34,23,45,__,__,__,__,__,12,23,12,63,__,__,34,34],
     [11,22,33,44,__,66,77,88,__,99,56,45,__,34,23,__,65,24,__,21,43,12,__,__,__,45,34,34,34,11,__,33,24,55,66,77,88,99,99,__,__,__,34,23,45,65,24,77,__,__,12,23,12,63,__,34,34,34],
     [11,22,33,44,__,66,77,88,__,99,56,45,34,34,23,__,__,24,__,__,43,12,__,12,__,45,34,34,34,11,__,__,__,__,__,__,__,99,__,45,34,34,23,45,__,24,77,21,__,__,99,__,__,__,__,__,34,34],
     [11,22,33,44,__,66,77,__,__,99,56,45,34,34,23,45,__,24,__,__,__,12,23,12,__,45,34,34,34,11,__,33,44,__,__,__,23,__,__,__,__,__,34,23,23,__,__,__,__,__,12,23,12,63,__,34,34,34],
     [11,22,33,44,__,__,__,__,__,99,56,45,34,34,23,45,__,34,__,21,__,__,__,__,__,45,__,34,34,__,__,__,44,__,66,77,88,99,99,56,45,__,34,23,__,__,24,77,21,43,12,23,12,63,__,34,34,34],
     [11,22,33,44,55,66,77,__,__,99,56,45,34,34,23,45,__,__,77,21,43,__,23,12,__,__,34,34,34,11,22,33,44,__,66,77,88,99,99,56,45,__,34,23,__,65,24,77,21,43,12,__,__,__,__,34,34,34],
     [11,22,33,44,55,66,77,88,__,99,56,45,34,34,23,45,65,00,77,__,__,__,23,12,63,__,34,34,34,11,22,33,44,__,__,__,88,99,99,__,45,__,34,23,__,__,24,77,21,43,12,__,44,63,__,34,34,34],
     [11,22,33,44,55,66,77,88,__,99,56,45,34,__,__,45,65,__,77,__,43,12,23,__,63,__,__,__,__,__,22,33,44,__,66,__,__,99,99,__,45,__,__,23,__,__,34,__,__,__,12,__,12,63,__,34,34,34],
     [11,22,33,44,55,66,77,88,__,99,56,45,34,34,__,__,__,__,77,__,__,__,__,__,63,45,34,34,34,__,22,33,44,__,66,77,__,99,99,__,45,34,__,23,__,65,__,77,21,__,__,__,__,63,__,__,'e',11],
     [11,22,33,44,55,__,__,__,__,99,56,45,__,__,__,45,65,24,77,21,43,12,23,__,__,45,34,34,34,__,22,33,44,__,66,77,__,__,99,__,__,__,__,23,__,65,__,77,21,__,12,23,__,63,45,45,34,34],
     [11,22,33,44,55,__,77,88,34,__,90,__,__,34,23,45,65,24,77,21,43,12,23,12,__,__,__,__,__,__,__,__,23,__,66,77,88,__,__,__,45,34,34,23,__,__,__,__,55,__,12,__,__,__,__,__,34,34],
     [11,22,33,44,55,__,77,88,__,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,__,34,34,__,22,33,44,55,66,77,88,99,99,__,45,34,34,43,34,65,__,77,21,__,__,__,12,63,45,34,34,34],
     [11,22,33,44,55,__,__,__,__,__,__,__,34,34,23,45,65,24,77,21,43,12,23,12,63,45,__,__,__,__,22,33,44,55,66,77,88,99,99,__,__,__,__,__,__,65,__,77,__,__,__,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,__,34,34,23,__,__,__,__,21,43,12,23,12,__,45,__,34,34,11,22,33,44,55,66,77,88,99,99,56,45,34,34,__,45,65,__,45,__,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,__,34,34,__,__,65,24,__,21,43,12,__,__,__,__,__,34,34,11,22,33,44,55,66,77,88,99,99,56,45,34,34,__,__,65,__,77,__,__,__,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,__,34,34,__,45,65,24,__,21,43,12,__,12,63,45,34,34,__,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,__,__,__,__,__,22,22,22,22,22,22,22,22,22], 
     [11,22,33,44,55,66,77,88,99,99,56,__,__,__,__,45,65,24,__,__,__,__,__,12,63,45,34,34,__,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,__,__,__,__,45,65,24,__,__,__,__,__,12,63,45,34,34,__,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,__,11,11,11,11,11,11,11,11,11,11,__,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],   
     [11,22,33,44,55,66,77,88,99,99,56,__,__,__,__,45,65,24,__,__,__,__,__,12,__,__,__,__,__,__,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,11,11,11,11,11,11,11,11,11,11,11,11,11,__,11,11,11,11,11,11,11,11,__,__,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],
     [11,22,33,44,55,66,77,88,99,__,__,__,__,__,__,45,65,24,__,__,__,__,__,__,63,45,34,34,__,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,__,56,__,23,__,65,24,77,21,__,12,__,__,__,45,34,34,__,__,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,11,23,34,34],
     [11,22,33,44,55,66,77,88,99,__,56,__,34,__,__,45,65,24,__,21,43,12,23,12,__,__,__,34,__,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,__,56,45,34,34,23,45,65,24,__,21,43,12,23,12,63,45,__,__,__,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,__,__,__,__,__,__,23,__,__,__,__,__,__,__,__,__,__,__,34,34,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34],
     [11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34,11,22,33,44,55,66,77,88,99,99,56,45,34,34,23,45,65,24,77,21,43,12,23,12,63,45,34,34,34]
     ]
    

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
            
            if MAP[i][j]:
                if MAP[i][j] =='p':
                     player.position = (i*5,0,j*5)

                     continue
                if MAP[i][j] == 'e':
                    exitdoor=EXIT(i,j)
                    continue

                wall = Entity(
                    model = 'cube',
                    scale = (5,20,5),
                    position = (i*5,0,j*5),
                    collider = 'box',
                    texture = r'textures\wood_cabinet_worn_long_diff_4k.jpg'
                    )
                




ground = Entity(
    model = 'plane',
    position = (0,0,0),
    scale = (1000,5,560),
    collider = 'mesh',
    color= color.blue
)


ground2 = Entity(
    model = 'plane',
    position = (0,-100,0),
    scale = (1000,5,560),
    collider = 'mesh',
    texture = r'이미지\스크린샷 2024-07-01 143235.png'
)

app.run()                                                                               
