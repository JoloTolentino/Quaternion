## Author          : Jolo Tolentino
## Project Name    : Quaternion Understanding through PyGame
## Project Started : February 25,2022

### I investigate the difference between the use of Euler Angles and Quaternions

#Hamilton’s Quaternions


# from numpy import angle
from Objects import Cube
import pygame
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Rotations import Euler_Angles, Quaternion
 
###
### basic py game to simulate Euler Angle rotation and quaternion
pygame.init()
display = (800,600)
pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
gluPerspective(45,(display[0]/display[1]),0.1,50.0) #
Object = Cube()
glTranslatef(0.0,0.0,-5)

# glRotatef(0,0,0,0)
print(type(glRotatef(0,0,0,0)))

Desired_Angle = 45
angle= 0 
pygame.time.delay(40)
while angle!= Desired_Angle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

    glRotatef(1, 0, 1, 1) # rotate using euler angles
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # refresh
    
    Object.create()
    pygame.display.flip()
    angle+=1
    pygame.time.wait(30)



