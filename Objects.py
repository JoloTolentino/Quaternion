## Author          : Jolo Tolentino
## Project Name    : Quaternion Understanding through PyGame and Matplotlib
## Project Started : February 25,2022

### I investigate the difference between the use of Euler Angles and Quaternions

#Hamilton’s Quaternions
 


from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *




class Cube: 
    def __init__ (self):
        self.vertices  =  [(1,-1,-1),
                            (1,1,-1),
                           (-1,1,-1),
                          (-1,-1,-1),
                            (1,-1,1),
                             (1,1,1),
                           (-1,-1,1),
                            (-1,1,1)]

        self.edges  = [(0,1),
                       (0,3),
                       (0,4),
                       (2,1),
                       (2,3),
                       (2,7),
                       (6,3),
                       (6,4),
                       (6,7),
                       (5,1),
                       (5,4),
                       (5,7)]
        
    
    def create(self):
        glBegin(GL_LINES)
        for edge  in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex]) #defining the vertex

        glEnd() 
