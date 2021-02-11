#########################
"""
Chaos Demo Using Python and simple game
"""
#########################

import numpy as np
import random
import matplotlib.pyplot as plt
import math


class Pattern:

    #empy array that will contain all the points to plot
    points = np.array(['no-points']);


    def __init__(self, bounding_points):
        self.n_bounds = len(bounding_points)/2
        #bounding points bounding_points[:0] -> x-points bounding_points[:,1] -> y-points
        self.bounding_points = np.reshape(np.array(bounding_points), (-1,2))
        self.points = np.array([])


    #returns midpoint of two points
    def findMidpoint(p1, p2):
        #find mids of x and y

        xmid = ( p1[0] + p2[0] ) / 2
        ymid = ( p1[1] + p2[1] ) / 2
        return [xmid, ymid]

    #loosen bounded requirement since starting point can really be anywhere
    def genRandPoint_Bounded(self):
        xmin = min(self.bounding_points[:,0])
        xmax = max(self.bounding_points[:,0])
        ymin = min(self.bounding_points[:,1])
        ymax = max(self.bounding_points[:,1])
        xrand = ( random.random()* (xmax-xmin) ) + xmin
        yrand = ( random.random()* (ymax-ymin) ) + ymin
        #random.random() returns random float between 0.0 and 1
        return [xrand, yrand]

    def rollDie( sides ):
        return int(round(random.random() * (sides-1) ) + 1)

    def addPoints(self, n ):
        p_start = Pattern.genRandPoint_Bounded(self)
        self.points = np.append(self.points, p_start)
        p_curr = p_start;
        while ( n > 0 ):
            die_sides = int(self.n_bounds)
            #print('Diesides: ',die_sides)
            dieroll = Pattern.rollDie(die_sides*2);
            #print('Dieroll: ', dieroll)
            #two different cases: die_sides = n_bounds ; die_sides = n_bounds*2
            if (die_sides == self.n_bounds):
                #die_sides number of ifs
                for i in range(die_sides):
                    #print('in for loop')
                    if (dieroll == i + 1):
                        #print('p_curr: ',p_curr,'   point: ', self.bounding_points[i])
                        p_curr = Pattern.findMidpoint(p_curr, self.bounding_points[i])
                        self.points = np.append(self.points, p_curr)
                        #print('next p: ', p_curr)
                        break
            #if dieroll == 3 0r 4 --> append(findMidpoint(p34, prand))
            if (die_sides == 2*self.n_bounds):
                #die_sides number of ifs
                for i in range(die_sides/2):
                    #print('in for loop')
                    if (int(math.floor(dieroll/2)) == i ):
                        #print('p_curr: ',p_curr,'   point: ', self.bounding_points[i])
                        p_curr = Pattern.findMidpoint(p_curr, self.bounding_points[i])
                        self.points = np.append(self.points, p_curr)
                        #print('next p: ', p_curr)
                        break
            n = n-1
    #plot the points_new
    def plotPoints(self, n):
        """
            things to add:
                *add animation
                *change styling
                    -different size dots
                    -different color for bounding points
        """
        self.addPoints(n)
        points_new = np.reshape(self.points,(-1,2))
        plt.scatter(self.bounding_points[:,0], self.bounding_points[:,1], s=20, c='red')
        plt.scatter(points_new[:,0], points_new[:,1], s=1, c='blue')
        plt.show()
