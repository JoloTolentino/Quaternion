from Objects import Cube
import pygame
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *





pygame.init()
display = (800,600)
pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
gluPerspective(45,(display[0]/display[1]),0.1,50.0) #
glTranslatef(0.0,0.0,-5)
glRotatef(0,0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

    glRotatef(1, 1, 1, 0) # rotate using euler angles
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # refresh
    Object = Cube()
    Object.create()
    pygame.display.flip()
    pygame.time.wait(10)


