# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:12:58 2017

@author: mullinwp

Main file
"""
import numpy as np
"""
Model outline
- Each person will walk to seats > put carry on away > get in their seats.
- Different list for each row. People are loading into their seats simultaniously.  

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

order = 0 # order will be imported list from other groups program.  
time = 0

def main(order):
    global time
    positions = np.linspace(0,-1*len(order),num=len(order),endpoint=False).astype(int)
    rows = np.arrary([row[0] for row in order])
    seated = emptyOrder(order)
    while(len(order)!=0):
        positions += 1 #Move Everyone forward
        time += 1 #Increment time, Work out units later
        order = lineSeating(positions,rows, order,seated)

def lineSeating(positions,rows, order,seated): 
    distance = positions - rows
    if (any(distance == 0)): #when rC - O = 0, the person has found their row.
        for i in range(len(distance)):
            if (distance[i]==0):
                enterRow(order[i],seated)  #where distance = 0, then start having that person start the seating process.
        
        #remove everone who left the seating line
        for i in range(len(distance)):
            if (distance[i]==0):
                order.remove(i) 
                
    #once they are seating it free's up the line behind them.
    return order
    
def enterRow(passenger,seated):
    global time
    #add random time if there is a passenger in between their seat and the isle 
    #put carry on away (RT)
    #enter seat "column" (RT)
    
def emptyOrder(order):
    emptyOrder = np.zeros((len(order),),dtype = 'i,i').tolist() #Credit: https://stackoverflow.com/questions/32561598/creating-tuples-with-np-zero
    return emptyOrder