# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:06:23 2017

@author: mullinwp
"""
import numpy as np
import numpy.random as random
import math
import PlaneLoad
#import PlaneLoad as pl



order = PlaneLoad.nzoneb2f(2)

class Passenger:
    def __init__(self,position,row,column):
        self.position = position
        self.row = row
        self.column = column
        self.canMove = True
        self.haltTime = 0
        self.isSeated = False
        
    def moveForeward(self):
        if self.canMove == True:
            self.position += 1
    
    def updateCanMove(self,other):
        if (other.position-1==self.position and other.canMove == False)or self.haltTime>0:
            self.canMove = False
            self.haltTime = other.haltTime
        else:
            self.canMove = True 
            
    def enterRow(self,wait):
        self.placeCarryOn()
        self.halt(math.ceil(random.exponential(5+wait*6)))
        
        
        
    def placeCarryOn(self):
        self.halt(math.ceil(random.exponential(15)))
        
    def halt(self,haltTime):
        self.haltTime += haltTime
        self.canMove = False
        
    def updateHaltTime(self):
        if self.haltTime == 0:
            self.canMove = True
        else:
            self.haltTime -= 1
    
    
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    
    def getHaltTime(self):
        return self.haltTime
    def setHaltTime(self,haltTime):
        self.haltTime = haltTime
        
    def getCanMove(self):
        return self.canMove
    def setCanMove(self,canMove):
        self.canMove = canMove
        
    def getIsSeated(self):
        return self.isSeated
    def setIsSeated(self,isSeated):
        self.isSeated = isSeated
        
def AirplaneSeatingSim(order):   
    time = 0
    seated = []
    order = buildOrder(order)
    notAllSeated = checkAllSeated(order)
    while (notAllSeated):
        for i in range(1,len(order)):
            order[i].updateCanMove(order[i-1])
        for i in range(len(order)):
            order[i].moveForeward()    
        time += 1
        for i in range(len(order)):
            order[i].updateHaltTime()
        order,seated = seating(order,seated)
        notAllSeated = checkAllSeated(order)
    return time
    
def seating(order,seated):
    distance=[]    
    for i in range(len(order)):
        distance.append(order[i].position-order[i].row)
    if (not(np.all(distance))): #when position - row = 0, the person has found their row.
        for i in range(len(distance)): 
            if (distance[i]==0 and not(order[i].getIsSeated())):
                extraWait = checkSeated(order[i],seated)
                order[i].enterRow(extraWait)  #where distance = 0, then start having that person start the seating process.
                for j in range(i+1,len(order)-1,1):
                    order[j].setHaltTime(order[i].getHaltTime()) #make everyone behind them stop
                order[i].setIsSeated(True) 
                seated.append(order[i])

#    #remove everone who left the seating line (everone whose distance=0 must have alread been seated)
#    for i in range(len(distance)):
#        if (distance[i]==0):
#            seated[i] = order[i]
#            order[i].setIsSeated(True) 

    return order,seated
    
    
#return the amount of seated people between the passenger and their seat
def checkSeated(passenger, seated):
    row = passenger.getRow()
    column = passenger.getColumn()
    wait = 0
    if column < 3:
        for i in range(len(seated)):
            if seated[i].getRow() ==row:
                if seated[i].getColumn()>column:
                    wait += 1
    else:
        for i in range(len(seated)):
            if seated[i].getRow() ==row:
                if seated[i].getColumn()<column:
                    wait += 1
    return wait
    
def buildOrder(order):
    tempOrder = []
    for i in range(len(order)):
        tempOrder.append(Passenger((-1*i)-1,order[i][0],order[i][1]))
    order = tempOrder[:len(order)]
    return order
    
#def emptyPlane(order):
#    planeRows = max([i[0] for i in order])
#    planeColumns = max([i[1] for i in order])
#    emptyPlane = np.zeros((planeRows,),dtype = 'i,'*planeColumns).tolist() #Credit: https://stackoverflow.com/questions/32561598/creating-tuples-with-np-zero 
#    return emptyPlane
#
#def emptyOrder(order):
#    emptyOrder = buildOrder(emptyPlane(order))
#    return emptyOrder
    
def longestHalt(order):
    longestHalt = 0
    for i in range(len(order)):
        if order[i].getHaltTime() > longestHalt:
            longestHalt = order[i].getHaltTime()
    return longestHalt

def checkAllSeated(order):
    for i in range(len(order)):
        if not(order[i].getIsSeated()):
            return True
    return False

randtotal =0
for i in range(100):
    randtotal += AirplaneSeatingSim(PlaneLoad.randomorder())
randtotal = randtotal/100

print("random order ",randtotal*2 ,"seconds")

b2ftotal =0
for i in range(100):
    b2ftotal += AirplaneSeatingSim(PlaneLoad.nzoneb2f(4))
b2ftotal = b2ftotal/100

print("4 zones ",b2ftotal*2,"seconds")

