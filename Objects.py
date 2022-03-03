## Author          : Jolo Tolentino
## Project Name    : Quaternion Understanding through PyGame and Matplotlib
## Project Started : February 25,2022

### I investigate the difference between the use of Euler Angles and Quaternions

#Hamilton’s Quaternions
 


from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

'To understand more about rotation I decided to creaete a Cube object to visualize the rotations'


class Cube: 

    "In 3D coordinate space, to draw a cube there are 8 vertexes ( yes those pointy edges)"
    "hence the 8 edges i predefined below."

    def __init__ (self):
        self.vertices  = [(1, -1,-1),
                          (1,  1,-1),
                          (-1, 1,-1),
                          (-1,-1,-1),
                          (1, -1, 1),
                          (1,  1, 1),
                          (-1,-1, 1),
                          (-1, 1, 1)]

        "In 3D coordinate space, to draw a cube there are 8 vertexes ( yes those pointy edges)"
        "hence the 8 edges i predefined below."

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
