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

def seating(order):
    rowCount = np.arrary(np.zeros(len(order)))
    t = 0    
    while(len(order)!=0):
        rowCount += 1
        t += 1 #Work out units later
        temp = rowCount - order
        if (any(temp == 0)): #when rC- O = 0, the person has found their row.
            #where temp = 0, then start having that person start the seating process.
        #start seating process. 
            #put carry on away (RT)
            #enter seat "column" (RT)
            #once they are seating it free's up the line behind them. 