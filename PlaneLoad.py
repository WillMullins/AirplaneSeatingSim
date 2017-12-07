# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:07:13 2017

@author: eastlarj
"""
import random
arriveorder = []
loadorder = []
lastgroup = []
aisle = 1
row = 1
ontimenumber = 150

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
    
def fivezoneb2f(arriveorder, loadorder, lastgroup, ontimenumber):
    zones = 5
    groupsize = 30/zones
    a = 1
    for zone in range(zones-1):
        for i in ontime:
            if (i[0] >=(31-groupsize*a)):
                loadorder.append(i)
            a +=1
    
        
        """for i in ontime:
            if (i[0] >=19):
                loadorder.append(i)
        for i in ontime:
            if (i[0] >=13):
                loadorder.append(i)
        for i in ontime:
            if (i[0] >=7):
                loadorder.append(i) """
    for i in ontime:
        if (i[0] <groupsize+1):
            lastgroup.append(i)
    
    lastgroup.extend(arriveorder[ontimenumber:])
    random.shuffle(lastgroup)
    
    loadorder.extend(lastgroup)
            
        
    print(loadorder)
    
    
    
#random(arriveorder, loadorder)
#twozoneb2f(arriveorder, loadorder, lastgroup, ontimenumber)
#twozonef2b(arriveorder, loadorder, lastgroup, ontimenumber)

fivezoneb2f(arriveorder, loadorder, lastgroup, ontimenumber)
