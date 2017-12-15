# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:12:58 2017

@author: mullinwp

Main file
"""
import numpy as np
import numpy.random as random
import PlaneLoad as pl
"""
Model outline
- Each person will walk to seats > put carry on away > get in their seats.
- Everyone who is at their row loads into their seats simultaniously.  

 - When walking to seats the line will simultaneously advance 1 row foreward
      if anyone in the line is at the row of their seat they will begin the 
      sitting down process
      
      all other people in line behind them will not advance in rows until that
      person is done sitting down
      
      1 person is at 1 row
      
 - the seating process will consist of 2 parts
     1) randomly, the passenger may have a carry on; if so they will spend a random
     amount of time putting it away
         for now we can assume the random variable will help take into account there
         being space for the carry on or not close to them
     2) Then the passenger will spend a random amount of time getting into their seat
         if there is already someone in that row between them and their seat this 
         random variable will (on average) increase.
"""

order = pl.randomorder()
print(order) # order will be imported list from other groups program.  
time = 0

def AirplaneSeatingSim(order):
    global time
    positions = np.linspace(0,-1*len(order),num=len(order),endpoint=False).astype(int) #position in line relative to 1 as the first row in the plane (they all start behind the first row)
    rows = np.arrary([row[0] for row in order]) #each individual's assigned row
    seated = emptyPlane(order)
    while(len(order)!=0):
        positions += 1 #Move Everyone forward
        time += 1 #Increment time, Work out units later (1 time unit is 2 seconds)
        order,seated = seating(positions,rows, order,seated)
    return time

def seating(positions,rows, order,seated): 
    distance = positions - rows
    if (any(distance == 0)): #when rC - O = 0, the person has found their row.
        for i in range(len(distance)):
            if (distance[i]==0):
                seated = enterRow(order[i],seated)  #where distance = 0, then start having that person start the seating process.
        
        #remove everone who left the seating line (everone whose distance=0 must have been seated first)
        for i in range(len(distance)):
            if (distance[i]==0):
                order.remove(i) 
                
    #once they are seating it free's up the line behind them.
    return order,seated
    
def enterRow(passenger,seated):
    global time
    row = passenger[0]-1
    column = passenger[1]-1
    placeCarryOn()
    if column < 3:
        if any(seated[row][:column])==True:
            #add random time if there is a passenger in between their seat and the isle 
            enterTime(np.count_nonzero(seated[row][:column]))
        else:
            enterTime(0)
    else:
        if any(seated[row][3:column])==True:
            enterTime(np.count_nonzero(seated[row][3:column]))
        else:
            enterTime(0)
            
    #put people into their row    
    seated[row][column] = seated[row][:column]+(1,)+seated[row][column+1:]        
    return seated
    
def emptyPlane(order):
    planeRows = max(order[:][0])
    planeColumns = max(order[:][1])
    emptyOrder = np.zeros((planeRows,),dtype = 'i,'*planeColumns).tolist() #Credit: https://stackoverflow.com/questions/32561598/creating-tuples-with-np-zero
    return emptyOrder
    
def placeCarryOn():
    global time
    time += random.exponencial(15) #this assumes an average of 30s to put a carry on away
    #add whatever time it takes to put a carry on away
    
def enterTime(wait):
    global time
    time += random.exponencial(5+wait*6) #assumes it takes 10s + 12s per person in your way 
    #add some amount to time
    
#totalTime = AirplaneSeatingSim(order)
#print("It took" + totalTime*2 + " seconds for everyone to be seated")