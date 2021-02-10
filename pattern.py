import numpy as np
import random
import matplotlib.pyplot as plt

#########################
"""


"""
#########################


class Pattern:

    #points defined as arrays [x,y]
    """
        TRIANGLE POSITIONING
               p34
                /\
            P12/__\P56
    """
    p12 = [2,0]
    p34 = [10,10]
    p56 = [18,0]

    m1234 = (p12[1]-p34[1]) / (p12[0]-p34[0])
    m1256 = (p12[1]-p56[1]) / (p12[0]-p56[0])
    m3456 = (p34[1]-p56[1]) / (p34[0]-p56[0])
    #if six sided die lands on corresponding number, midpoint to that point

    #empy array that will contain all the points to plot
    points = np.array([]);


    #returns midpoint of two points
    def findMidpoint(p1, p2):
        #find mids of x and y
        xmid = ( p1[0] + p2[0] ) / 2
        ymid = ( p1[1] + p2[1] ) / 2
        return [xmid, ymid]

    def isNotInBounds (p):
        #yp = mxp - mx1 + y1
        y1 = Pattern.m1234*p[0] - Pattern.m1234*Pattern.p12[0] + Pattern.p12[1]
        y2 = Pattern.m1256*p[0] - Pattern.m1256*Pattern.p12[0] + Pattern.p12[1]
        y3 = Pattern.m3456*p[0] - Pattern.m3456*Pattern.p34[0] + Pattern.p34[1]
        #print(y1)
        #print(y2)
        #print(y3)
        #P[1] must be >y2 , <y1, <y3
        if ( p[1] > y2 and p[1] < y1 and p[1] < y3):
            return False
        else:
            return True

    def genRandPoint_Bounded():
        xmin = min(Pattern.p12[0], Pattern.p34[0], Pattern.p56[0])
        xmax = max(Pattern.p12[0], Pattern.p34[0], Pattern.p56[0])
        ymin = min(Pattern.p12[1], Pattern.p34[1], Pattern.p56[1])
        ymax = max(Pattern.p12[1], Pattern.p34[1], Pattern.p56[1])
        xrand = ( random.random()* (xmax-xmin) ) + xmin
        yrand = ( random.random()* (ymax-ymin) ) + ymin
        while ( Pattern.isNotInBounds([xrand, yrand]) ):
            xrand = ( random.random()* (xmax-xmin) ) + xmin
            yrand = ( random.random()* (ymax-ymin) ) + ymin
        #random.random() returns random float between 0.0 and 1
        return [xrand, yrand]

    def rollDie( sides ):
        return round(random.random() * (sides-1) ) + 1

    def addPoints( n ):
        p_start = Pattern.genRandPoint_Bounded()
        Pattern.points = np.append(Pattern.points, p_start)
        p_curr = p_start;
        while ( n > 0 ):
            dieroll = Pattern.rollDie(6);
            #if dieroll == 1 0r 2 --> append(findMidpoint(p12, prand))
            if ( dieroll == 1 or dieroll == 2 ):
                p_curr = Pattern.findMidpoint(Pattern.p12, p_curr)
                Pattern.points = np.append(Pattern.points, p_curr )
            #if dieroll == 3 0r 4 --> append(findMidpoint(p34, prand))
            if ( dieroll == 3 or dieroll == 4 ):
                p_curr = Pattern.findMidpoint(Pattern.p34, p_curr)
                Pattern.points = np.append(Pattern.points, p_curr )
            #if dieroll == 5 0r 6 --> append(findMidpoint(p56, prand))
            if ( dieroll == 5 or dieroll == 6 ):
                p_curr = Pattern.findMidpoint(Pattern.p56, p_curr)
                Pattern.points = np.append(Pattern.points, p_curr )
            n = n-1


Pattern.addPoints(1000)
points = np.reshape(Pattern.points, (-1,2))
x = points[:,0]
y = points[:,1]
plt.scatter(x,y)
plt.show()
