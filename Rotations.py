## Author          : Jolo Tolentino
## Project Name    : Quaternion Understanding through PyGame
## Project Started : February 25,2022

### I investigate the difference between the use of Euler Angles and Quaternions

#Hamilton’s Quaternions
import numpy as np 
import math as m
import matplotlib.pyplot as plt 

class Rotation:
    def __init__(self,yaw, pitch, roll ):
        self.yaw = yaw # Rotation along the X axis 
        self.pitch = pitch # Rotation along the Y axis
        self.roll = roll # Rotation along the Z axis

class Euler_Angles(Rotation):
    def __init__(self,yaw,pitch,roll):
        super().__init__(yaw,pitch,roll)
        self.initial_frame = (1,1,1)
    def Rotation_X(self):
        pass


class Quaternion(Rotation) :
    def __init__ (self,yaw,pitch,roll,Rotation_matrix = None):
        super().init(yaw,pitch,roll)
        if Rotation_matrix: 
            self.phi,self.theta,self.psi = Rotation_matrix
    def rotate(self,q1, v1):
        q2 = (0.0,) + v1
        
        print(q2)
        return self.multiply(self.multiply(q1, q2), self.conjugate(q1))[1:]


    def rotate2(self,q1, v1):
        q2 = (0.0,) + v1
        # print("Q2 : ")
        print(q2)
        return self.multiply(self.multiply(q2, q1), self.conjugate(q2))[1:]

    def conjugate(self,quarterion):
        #quarterrions = w,x,y,z and their conjugates are w,-x,-y,-z
        return (quarterion[0],-quarterion[1],-quarterion[2],-quarterion[3])

    def multiply(self,quarterion1,quarterion2):
        w1, x1, y1, z1 = quarterion1
        w2, x2, y2, z2 = quarterion2
        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
        z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
        return w, x, y, z

    def euler_to_quaternion(phi, theta, psi):
 
        qw = np.cos(phi/2) * np.cos(theta/2) * np.cos(psi/2) + np.sin(phi/2) * np.sin(theta/2) * np.sin(psi/2)
        qx = np.sin(phi/2) * np.cos(theta/2) * np.cos(psi/2) - np.cos(phi/2) * np.sin(theta/2) * np.sin(psi/2)
        qy = np.cos(phi/2) * np.sin(theta/2) * np.cos(psi/2) + np.sin(phi/2) * np.cos(theta/2) * np.sin(psi/2)
        qz = np.cos(phi/2) * np.cos(theta/2) * np.sin(psi/2) - np.sin(phi/2) * np.sin(theta/2) * np.cos(psi/2)
 
        return [qw, qx, qy, qz]

    def quaternion_to_euler(q0, q1, q2, q3):
     
        X = m.atan2((2*(q0*q1+q2*q3)), (1-2*(q1*q1+q2*q2)))
        Y = m.asin(1 if 2 * (q0 * q2 - q3 * q1) > 1 else (-1 if 2 * (q0 * q2 - q3 * q1)<-1 else 2 * (q0 * q2 - q3 * q1)))
        Z = m.atan2((2*(q0*q3 + q1*q2)),(1-2*(q2*q2+q3+q3)))
 
        return X, Y, Z




	
v1 = (1,0,0)

phi = m.pi/2
theta = m.pi/4
psi = m.pi/2
q = Quaternion.euler_to_quaternion(phi, theta, psi)

print(q)

test = Quaternion()
#rotation based on
v2 = test.rotate(q,v1)


v3 = test.rotate2(q,v1)
print(np.round(v2, decimals=2))
# print(np.round(v3, decimals=2))

import matplotlib.pyplot as plt
  
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Cartesian axes
ax.quiver(-1, 0, 0, 3, 0, 0, color='#aaaaaa',linestyle='dashed')
ax.quiver(0, -1, 0, 0,3, 0, color='#aaaaaa',linestyle='dashed')
ax.quiver(0, 0, -1, 0, 0, 3, color='#aaaaaa',linestyle='dashed')
# Vector before rotation
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='b')
# Vector after rotation
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='r')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='g')
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
plt.show()
