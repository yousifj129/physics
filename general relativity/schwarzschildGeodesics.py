import torch
import math
import string
massearth = 5.972e24
radiusearth = 6371000
x = [0,radiusearth,5,10]
xv = [1,0,5,1]
#cot function (its not available in the math library)
def cot(theta):
    tangent_value = math.tan(theta)
    
    # Check if tangent_value is zero to avoid division by zero
    if tangent_value == 0:
        return 0
    
    return 1 / tangent_value
def solveChristoffel(xcord, xvel , M , G , c):
    
    
    accelerationTime = -(2 * ((G * M / xcord[1]**2 ) * (1- (2*G * M/ (xcord[1] * c**2)))**-1)) * xvel[0] * xvel[1]
    
    
    accelerationPhi = -(((2/xcord[1]) * xvel[1] * xvel[3]) + (2 * cot(xcord[2]) * xvel[2] * xvel[3]))
    
    
    accelerationTheta = -(((2/xcord[1]) * xvel[1] * xvel[2]) + (-math.sin(xcord[2]) * math.cos(xcord[2]) * xvel[3]**2) )
    
    
    accelerationR = -(((G * M / xcord[1]**2 ) * (1- (2*G * M/ (xcord[1] * c**2))) * xvel[0]**2)
                       + ((G * M / xcord[1]**2 ) * (1- (2*G * M/ (xcord[1] * c**2)))**-1) * xvel[1]**2
                        + ((-xcord[1] * (1- (2*G * M/ (xcord[1] * c**2))) * xvel[2]**2 )) 
                        +((-xcord[1] * math.sin(xcord[2]) * (1- (2*G * M/ (xcord[1] * c**2))) * xvel[3]**2 )))
    
    
    stf = ("accelerationTime = " + str(accelerationTime) 
           + "     accelerationR = " + str(accelerationR) 
           + "     accelerationTheta = " + str(accelerationTheta) 
           + "     accelerationPhi = " + str(accelerationPhi))
    print(stf)
    return [accelerationTime,accelerationR,accelerationTheta,accelerationPhi]

G = 6.6743e-11
c = 299792458
for i in range(10):
    accelerations = solveChristoffel(x,xv,massearth, G,c)
    x[0] = x[0] + xv[0] * xv[0] + 0.5 * accelerations[0] * xv[0]**2
    x[1] = x[1] + xv[1] * xv[0] + 0.5 * accelerations[1] * xv[0]**2
    x[2] = x[2] + xv[2] * xv[0] + 0.5 * accelerations[2] * xv[0]**2
    x[3] = x[3] + xv[3] * xv[0] + 0.5 * accelerations[3] * xv[0]**2

    stf = ("pos time = " + str(x[0]) 
           + "     pos R = " + str(x[1]) 
           + "     pos Theta = " + str(x[2]) 
           + "     pos Phi = " + str(x[3]))
    print(stf)

