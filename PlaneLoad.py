# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:07:13 2017

@author: eastlarj
"""
import random
import math
loadorder = []
lastgroup = []


#create random arrival order


def randomorder():
    arriveorder=[]
    aisle = 1
    row = 1
    
    while (row <= 30):
        arriveorder.append((row, aisle))
        if (aisle == 6):
            row += 1
            aisle = 0
        aisle +=1
    random.shuffle(arriveorder)
    #print("Arrive order =",arriveorder)
    return arriveorder
    
def nzoneb2f(n):
    loadorder = []   
    zones = n
    rowchunk = 30/zones
    a = 1
    ontimenumber = random.randint(100,170)
    arriveorder = randomorder()
    ontime = arriveorder[0:ontimenumber]
    latepeople = arriveorder[ontimenumber:]
    
    #DISTRIBUTION OF LATE PEOPLE BY ZONE
    alpha = random.random()*3 + 3
    dy = 0
    latezones = []
    totallate = len(latepeople)
    #print("Number late =",totallate)
    for i in range(zones-1):
        dy = abs(math.exp(-alpha*(i))-math.exp(-alpha*((1+i)*(1/zones))))
        latezones.append(int(round(dy*totallate)))
    latezones.append(totallate-sum(latezones))
   # print("Number of people arriving late during each zone =",latezones)
    
    #LOAD 'EM UP
    nowarrived = []
    for zone in range(zones):
        for i in ontime:
            if (i[0] >=(31-rowchunk*a) and i[0] <= 30-rowchunk*(a-1)):
                loadorder.append(i)
        nowarrived = latepeople[:latezones[zone]]
        del latepeople[:latezones[zone]]
        for i in nowarrived:
            if i[0]>=(31-rowchunk*a):
                loadorder.append(i)
            else:
                ontime.append(i)   
        a += 1
        
    for i in loadorder:
        for t in loadorder:
            if i == t and loadorder.index(i) != loadorder.index(t):
                print("Well, shit")
    
    
    #print("Load order =",loadorder)
    return loadorder
    


nzoneb2f(3)
