# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:07:13 2017

@author: eastlarj
"""
import random
import math
arriveorder = []
loadorder = []
lastgroup = []
aisle = 1
row = 1
ontimenumber = random.randint(100,170)

#create random arrival order
while (row <= 30):
    arriveorder.append((row, aisle))
    if (aisle == 6):
        row += 1
        aisle = 0
    aisle +=1
    
random.shuffle(arriveorder)
#print(arriveorder)

ontime = arriveorder[0:ontimenumber]
latepeople = arriveorder[ontimenumber:]

def randomorder(arriveorder, loadorder):
    loadorder = arriveorder
    return loadorder

def twozoneb2f(arriveorder, loadorder, lastgroup, ontimenumber):
    #shmucks in the back who showed up on time
    for i in ontime:
        if (i[0] >15):
            loadorder.append(i)
        
    #bougie peeps
    for i in ontime:
        if (i[0] <16):
            lastgroup.append(i)
    
    #mix in late losers to last boarding group
    lastgroup.extend(arriveorder[ontimenumber:])
    random.shuffle(lastgroup)
    
    loadorder.extend(lastgroup)
    
    return loadorder
    
def twozonef2b(arriveorder, loadorder, lastgroup, ontimenumber):
    
    #bougie peeps who showed up on time
    for i in ontime:
        if (i[0] <16):
            lastgroup.append(i)    
            
    #shmucks in the back
    for i in ontime:
        if (i[0] >15):
            loadorder.append(i)
    
    #mix in late losers to last boarding group
    lastgroup.extend(arriveorder[ontimenumber:])
    random.shuffle(lastgroup)
    
    loadorder.extend(lastgroup)
    
    return loadorder
    
def nzoneb2f(n, arriveorder, loadorder, lastgroup, ontime, ontimenumber, latepeople):
    zones = n
    rowchunk = 30/zones
    a = 1
    
    #DISTRIBUTION OF LATE PEOPLE BY ZONE
    alpha = random.random()*3 + 3
    dy = 0
    latezones = []
    totallate = len(latepeople)
    print(totallate)
    for i in range(zones-1):
        dy = abs(math.exp(-alpha*(i))-math.exp(-alpha*((1+i)*(1/zones))))
        latezones.append(int(round(dy*totallate)))
    latezones.append(totallate-sum(latezones))
    print(latezones)
    
    #LOAD 'EM UP
    nowarrived = []
    print(latepeople)
    for zone in range(zones):
        for i in ontime:
            if (i[0] >=(31-rowchunk*a) and i[0] <= 30-rowchunk*(a-1)):
                loadorder.append(i)
        nowarrived = latepeople[:latezones[zone]]
        del latepeople[:latezones[zone]]
        print(latepeople)
        for i in nowarrived:
            if i[0]>=(31-rowchunk*a):
                loadorder.append(i)
            else:
                ontime.append(i)   
        a += 1
        
    print(loadorder)
    print(len(loadorder))
    
    
    
#random(arriveorder, loadorder)
#twozoneb2f(arriveorder, loadorder, lastgroup, ontimenumber)
#twozonef2b(arriveorder, loadorder, lastgroup, ontimenumber)

nzoneb2f(3, arriveorder, loadorder, lastgroup, ontime, ontimenumber, latepeople)
