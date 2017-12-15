# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:06:23 2017

@author: mullinwp
"""
import numpy as np
import numpy.random as random


time = 0
order = 0

class Passenger:
    def __init__(self,position,row,column):
        self.position = position
        self.row = row
        self.column = column
        self.canMove = True
        self.haltTime = 0
        
    def moveForeward(self):
        if self.canMove == True:
            self.position += 1
    
    def updateMove(self,other):
        if (other.postition+1==self.position & other.canmove == False)| self.haltTime>0 :
            self.canMove = False
            self.haltTime = other.haltTime
        else:
            self.canMove = True 
            
    def enterRow(self,seated,wait):
        self.placeCarryOn()
        self.haltTime += round(random.exponencial(15))
        
        
    def placeCarryOn(self):
        self.halt(round(random.exponencial(15)))
        
    def halt(self,haltTime):
        self.haltTime = haltTime
        self.canMove = False
        
    def update(self):
        global time
        time += 1
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
        
def AirplaneSeatingSim(order):
    buildOrder(order)
    seated = emptyPlane(order)
    while (len(order) != 0):
        for i in range(len(order)-1):
            order[i].updateMove([i+1])
        order.moveForeward()
        order.update()
        order,seated = seating(order,seated)
    
def seating(order,seated):
    distance = order.position-order.rows
    if (any(distance == 0)): #when rC - O = 0, the person has found their row.
      #we need to have the "simultaneous" seating start from the from of the line for halt time purposes.
      for i in range(len(distance)-1,-1,-1): #Found this here https://stackoverflow.com/questions/869885/loop-backwards-using-indices-in-python
          if (distance[i]==0):
              extraWait = checkSeated(order[i],seated)
              order[i].enterRow(seated,extraWait)  #where distance = 0, then start having that person start the seating process.
              order[:i].setHaltTime(order[i].getHaltTime()) #make everyone behind them stop

    #remove everone who left the seating line (everone whose distance=0 must have alread been seated)
    for i in range(len(distance)):
        if (distance[i]==0):
            order.remove(i)    

    return order,seated
    
    
#return the amount of seated people between the passenger and their seat
def checkSeated(passenger, seated):
    row = passenger.getRow()
    column = passenger.getColumn()
    if column < 3:
        if any(seated[row][:column])==True:

            return np.count_nonzero(seated[row][:column])
        else:
            return 0
    else:
        if any(seated[row][3:column])==True:
            return np.count_nonzero(seated[row][3:column])
        else:
            return 0
    
def buildOrder(order):
    tempOrder = emptyPlane(order)
    for i in range(len(order)):
        tempOrder[i] = Passenger(-1*i,order[i][1],order[i][2])
    order = tempOrder
    
def emptyPlane(order):
    planeRows = max(order[:][0])
    planeColumns = max(order[:][1])
    emptyOrder = np.zeros((planeRows,),dtype = 'i,'*planeColumns).tolist() #Credit: https://stackoverflow.com/questions/32561598/creating-tuples-with-np-zero
    return emptyOrder