#Hanpilton’s Quaternions
import numpy as np 
import matplotlib.pyplot as plt 

class Quaternion:
    def __init__ (self,Rotation_matrix = None):
        if Rotation_matrix: 
            self.phi,self.theta,self.psi = Rotation_matrix



    def conjugate(quarterion):
        #quarterrions = w,x,y,z and their conjugates are w,-x,-y,-z
        return (quarterion[0],-quarterion[1],-quarterion[2],-quarterion[3])
    
    def multiply(quarterion1,quarterion2):
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



