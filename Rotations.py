## Author          : Jolo Tolentino
## Project Name    : Quaternion Understanding through PyGame and Matplotlib
## Project Started : February 25,2022

### I investigate the difference between the use of Euler Angles and Quaternions

#Hamilton’s Quaternions
import numpy as np 
import math as m
import matplotlib.pyplot as plt 
import sys

class Rotation:
    def __init__(self,yaw, pitch, roll ):
        self.yaw = yaw*(np.pi/180) # Rotation along the X axis 
        self.pitch = pitch*(np.pi/180) # Rotation along the Y axis
        self.roll = roll*(np.pi/180) # Rotation along the Z axis


class Euler_Angles(Rotation):
    
    def __init__(self,yaw,pitch,roll):
        super().__init__(yaw,pitch,roll)
        self.initial_frame = (1,1,1)
    

    ### Established rotations
    ## the columns represent the rotation 
    
    def Rotation_X(yaw):
        return np.matrix([[ 1, 0           , 0       ],
                          [ 0, m.cos(yaw),-m.sin(yaw)],
                          [ 0, m.sin(yaw), m.cos(yaw)]])
            
    def Rotation_Y(pitch):
        return np.matrix([[ m.cos(pitch), 0, m.sin(pitch)],
                          [ 0           , 1, 0           ],
                          [-m.sin(pitch), 0, m.cos(pitch)]])
  

    def Rotation_Z(roll): 
        return np.matrix([[ m.cos(roll), -m.sin(roll), 0 ],
                          [ m.sin(roll), m.cos(roll) , 0 ],
                          [ 0         , 0            , 1 ]])


    def Cardan_Angles(matrix): #rotation about 3 Axis (X,Y,Z)
        tol = sys.float_info.epsilon * 10
        
        if abs(matrix.item(0,0))< tol and abs(matrix.item(1,0)) < tol:
            eul1 = 0
            eul2 = m.atan2(-matrix.item(2,0), matrix.item(0,0))
            eul3 = m.atan2(-matrix.item(1,2), matrix.item(1,1))

        else:   
            eul1 = m.atan2(matrix.item(1,0),matrix.item(0,0))
            sp = m.sin(eul1)
            cp = m.cos(eul1)
            eul2 = m.atan2(-matrix.item(2,0),cp*matrix.item(0,0)+sp*matrix.item(1,0))
            eul3 = m.atan2(sp*matrix.item(0,2)-cp*matrix.item(1,2),cp*matrix.item(1,1)-sp*matrix.item(0,1))
        
        return eul1,eul2,eul3





## Enter the Unknown 
'Quaternions can represent 3D rotation, and is arguably the better option over Euler Angles'
'Due to human nature, we always opt for the easier solution if it would suffice'
'But for our application we need to delve deeper into the 3D spatial mathematics to generate stability'

class Quaternion(Rotation) :
    def __init__ (self,yaw,pitch,roll,Rotation_matrix = None):
        if Rotation_matrix: 
            self.phi,self.theta,self.psi = Rotation_matrix
        else: 
            super().__init__(yaw, pitch,roll)
            self.phi,self.theta, self.psi = self.yaw,self.pitch,self.roll
        
    def Rotate(self,q1, v1):
        q2 = (0.0,) + v1
        return self.multiply(self.multiply(q1, q2), self.conjugate(q1))[1:]


    def Conjugate(self,quarterion):
        #quarterrions = w,x,y,z and their conjugates are w,-x,-y,-z
        return (quarterion[0],-quarterion[1],-quarterion[2],-quarterion[3])

    def Multiply(self,quarterion1,quarterion2):
        w1, x1, y1, z1 = quarterion1
        w2, x2, y2, z2 = quarterion2
        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
        z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
        return w, x, y, z

    def Euler_to_Quaternion(phi, theta, psi):
 
        qw = np.cos(phi/2) * np.cos(theta/2) * np.cos(psi/2) + np.sin(phi/2) * np.sin(theta/2) * np.sin(psi/2)
        qx = np.sin(phi/2) * np.cos(theta/2) * np.cos(psi/2) - np.cos(phi/2) * np.sin(theta/2) * np.sin(psi/2)
        qy = np.cos(phi/2) * np.sin(theta/2) * np.cos(psi/2) + np.sin(phi/2) * np.cos(theta/2) * np.sin(psi/2)
        qz = np.cos(phi/2) * np.cos(theta/2) * np.sin(psi/2) - np.sin(phi/2) * np.sin(theta/2) * np.cos(psi/2)
 
        return [qw, qx, qy, qz]

    def Quaternion_to_Euler(q0, q1, q2, q3):
     
        X = m.atan2((2*(q0*q1+q2*q3)), (1-2*(q1*q1+q2*q2)))
        Y = m.asin(1 if 2 * (q0 * q2 - q3 * q1) > 1 else (-1 if 2 * (q0 * q2 - q3 * q1)<-1 else 2 * (q0 * q2 - q3 * q1)))
        Z = m.atan2((2*(q0*q3 + q1*q2)),(1-2*(q2*q2+q3+q3)))
 
        return X, Y, Z




	
# v1 = (1,0,0)

# phi = m.pi/2
# theta = m.pi/4
# psi = m.pi/2
# q = Quaternion.euler_to_quaternion(phi, theta, psi)

# print(q)

# test = Quaternion(0,0,0)
# #rotation based on
# v2 = test.rotate(q,v1)


# # v3 = test.rotate2(q,v1)
# print(np.round(v2, decimals=2))
# # print(np.round(v3, decimals=2))

# import matplotlib.pyplot as plt
  
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# # Cartesian axes
# ax.quiver(-1, 0, 0, 3, 0, 0, color='#aaaaaa',linestyle='dashed')
# ax.quiver(0, -1, 0, 0,3, 0, color='#aaaaaa',linestyle='dashed')
# ax.quiver(0, 0, -1, 0, 0, 3, color='#aaaaaa',linestyle='dashed')
# # Vector before rotation
# ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='b')
# # Vector after rotation
# ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='r')
# # ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='g')
# ax.set_xlim([-1.5, 1.5])
# ax.set_ylim([-1.5, 1.5])
# ax.set_zlim([-1.5, 1.5])
# plt.show()
