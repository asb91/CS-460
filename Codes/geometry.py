import math

#CALCULATES DISTANCE
    
def distance(x1,y1,z1,x2,y2,z2):
    dist= ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2)
    dist = math.sqrt(dist)
    return dist

# CALCULATES ANGLE

def angle(x1,y1,z1,x2,y2,z2):
    dot_prod = (x2*x1) + (y2*y1) + (z2*z1)
    mag1 = math.sqrt(((x1)**2) + ((y1)**2) + ((z1)**2))
    mag2 = math.sqrt(((x2)**2) + ((y2)**2) + ((z2)**2))
    ang = math.acos((dot_prod)/(mag1*mag2))*(180/math.pi)
    return ang
