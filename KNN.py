import random
import csv
from math import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import csv
plt.close("all")

# 81 & 165
sec1=[[3,3], [5,8], [5,2], [8,2], [1,0], [5,5], [6,7], [0,2], [7,3], [0,9], [6,1], [3,5], [7,0], [5,7], [2,2], [3,3], [4,5], [3,8], [2,7], [2,8], [4,5], [5,6], [2,8], [7,5], [1,1], [4,1], [1,5], [5,4], [4,9], [1,2], [0,7], [1,8], [0,0], [1,4], [1,2], [0,6], [6,0], [9,1], [2,6], [3,3], [6,2], [7,4], [7,6], [7,2], [8,3], [2,9], [0,1], [4,8], [0,6], [1,8], [0,5], [8,0], [0,0], [2,6], [7,2], [6,4], [6,4], [4,4], [4,5], [8,4], [6,0], [2,3], [0,0], [8,1], [3,4], [5,1], [3,5], [7,0], [0,2], [4,1], [1,9], [8,3], [0,1], [2,9], [5,4], [4,7], [3,3], [1,4], [8,0], [0,6], [3,1]]
sec2=[[20,30], [20,24], [21,22], [23,23], [20,22], [30,27], [23,23], [23,25], [24,30], [28,29], [20,24], [24,26], [29,27], [22,26], [25,22], [24,29], [24,28], [28,27], [25,29], [25,26], [23,24], [29,26], [29,30], [23,24], [23,30], [28,25], [22,22], [29,28], [27,20], [27,22], [29,20], [27,28], [30,24], [28,27], [30,30], [30,29], [28,23], [22,25], [24,24], [25,22], [29,24], [25,23], [27,22], [25,30], [27,28], [23,27], [20,22], [21,30], [22,30], [20,20], [22,20], [24,24], [23,29], [26,23], [28,25], [28,26], [28,23], [20,25], [21,24], [24,29], [20,29], [20,28], [29,28], [30,28], [29,20], [21,21], [28,24], [22,29], [24,23], [25,23], [25,27], [26,22], [28,25], [28,28], [30,23], [25,28], [22,25], [26,24], [20,28], [30,23], [26,21], [23,26], [22,29], [22,30], [27,29], [29,20], [22,30], [27,25], [26,27], [28,21], [25,22], [25,27], [21,22], [20,26], [23,21], [27,26], [25,22], [27,20], [26,20], [23,24], [23,20], [21,25], [28,23], [27,28], [22,25], [25,21], [23,28], [20,25], [29,23], [22,29], [27,30], [30,23], [28,23], [29,20], [28,23], [20,26], [30,26], [23,29], [23,25], [24,26], [28,25], [30,28], [24,26], [29,21], [22,27], [28,23], [24,20], [26,22], [22,27], [22,29], [22,29], [25,26], [22,24], [20,27], [28,30], [28,23], [25,21], [28,26], [29,28], [23,21], [25,27], [25,28], [22,27], [28,23], [30,30], [23,20], [24,29], [28,25], [30,28], [28,23], [27,22], [26,28], [29,25], [23,26], [21,21], [28,29], [20,22], [25,21], [27,21], [23,26], [21,22], [29,20], [20,27], [22,28], [25,21]]
testingsec=[[16,20], [11,18], [14,17], [16,15], [12,19], [20,14], [18,11], [14,17], [19,16], [15,17], [13,16], [18,15], [17,18], [18,14], [17,16], [20,18], [17,12], [16,14], [17,19], [16,18], [16,19], [20,13], [15,15], [17,14], [12,20], [18,20], [16,19], [17,16], [13,18], [18,14], [13,18], [16,19], [15,19], [17,19], [18,20], [20,13], [19,10], [16,20], [18,16], [14,15], [14,18], [12,17], [15,14], [19,13], [18,20], [18,14], [12,18], [20,13], [15,15], [18,19], [10,18], [18,17], [16,13], [13,17], [20,20], [20,18], [13,17], [19,16], [16,15], [19,10], [17,11], [18,18], [15,20], [15,18], [14,18], [15,16], [13,18], [11,19], [19,14], [20,12], [20,13], [11,20], [12,19], [19,20], [19,13], [19,11], [20,15], [11,17], [20,10], [20,11], [19,12], [12,19], [12,19], [18,18], [13,18], [19,11], [18,20], [16,19], [15,15], [18,20], [17,17], [14,15], [17,20], [17,16], [14,18], [10,20], [14,18], [10,18], [11,20], [18,12], [14,17], [10,19], [17,18], [20,10], [13,20], [13,19], [17,14], [19,15], [18,20], [14,18], [17,13], [20,13], [16,16], [12,18], [17,13], [19,17], [19,14], [18,20], [20,13], [19,13], [17,17], [19,19], [19,18], [20,18], [19,10], [18,12], [19,18], [20,12], [19,12], [12,20], [19,11], [20,20], [14,19], [16,15], [12,19], [17,13], [15,15], [14,15], [15,20], [20,13], [20,16], [20,18], [20,11], [11,20], [20,11], [19,11], [18,10], [20,20], [16,16], [16,16], [13,18], [19,14], [18,10], [19,11], [19,14], [17,19], [11,18], [12,20], [19,19], [20,18], [19,20], [18,17], [16,16], [18,18], [19,19], [16,15], [13,20], [18,20], [17,19], [17,13], [18,14], [16,16], [17,12], [18,17], [10,19], [16,17], [19,14], [20,15], [15,16], [15,16], [13,20], [15,20], [16,13], [20,13], [19,17], [19,12], [17,19], [12,18], [20,17], [16,13], [12,18], [12,20], [20,17], [13,18], [20,10], [17,16], [10,18], [17,17], [17,12], [20,13], [13,17], [20,19], [16,17], [16,18], [13,19], [15,19], [10,18], [10,18], [12,19], [19,16], [16,20], [20,11], [12,17], [18,20], [16,18], [20,15], [15,14], [19,14], [19,12], [16,18], [14,20], [18,16], [16,19], [19,13], [18,12], [17,11], [11,19], [16,14], [11,17], [20,11], [14,18], [18,13], [19,16], [12,19], [14,17], [12,20], [17,16], [15,15], [20,20], [20,16], [19,19], [17,15], [19,14], [18,13], [15,15], [20,11], [12,18], [12,18], [18,10], [17,11], [19,15], [19,15], [13,18], [20,19], [18,13], [14,17], [17,14], [18,20], [19,18], [18,14], [19,16], [20,19], [20,15], [15,17], [16,18], [19,14], [14,15], [15,17], [11,17], [17,13], [17,16], [19,15], [16,16], [18,14], [16,20], [18,12], [12,20], [16,17], [17,20], [14,19], [17,18], [18,10], [13,17], [15,18], [17,15], [17,19], [20,14], [20,14], [15,16], [18,17], [19,13], [15,16], [17,19], [19,11], [17,11], [15,19], [20,10], [14,19], [17,11], [17,18], [15,16], [13,16], [18,16], [17,12], [17,15], [16,18], [20,19], [16,15], [14,17], [20,18], [16,14], [18,17], [18,18], [18,14], [18,10], [19,18], [18,20], [10,20], [16,14], [18,19], [13,17], [18,17], [20,15], [17,18], [17,20]]
ss1=[[3,3], [5,8], [5,2], [8,2], [1,0], [5,5], [6,7], [0,2], [7,3], [0,9], [6,1], [3,5], [7,0], [5,7], [2,2], [3,3], [4,5], [3,8], [2,7], [2,8], [4,5], [5,6], [2,8], [7,5], [1,1], [4,1], [1,5], [5,4], [4,9], [1,2], [0,7], [1,8], [0,0], [1,4], [1,2], [0,6], [6,0], [9,1], [2,6], [3,3], [6,2], [7,4], [7,6], [7,2], [8,3], [2,9], [0,1], [4,8], [0,6], [1,8], [0,5], [8,0], [0,0], [2,6], [7,2], [6,4], [6,4], [4,4], [4,5], [8,4], [6,0], [2,3], [0,0], [8,1], [3,4], [5,1], [3,5], [7,0], [0,2], [4,1], [1,9], [8,3], [0,1], [2,9], [5,4], [4,7], [3,3], [1,4], [8,0], [0,6], [3,1]]

ss2=[[20,30], [20,24], [21,22], [23,23], [20,22], [30,27], [23,23], [23,25], [24,30], [28,29], [20,24], [24,26], [29,27], [22,26], [25,22], [24,29], [24,28], [28,27], [25,29], [25,26], [23,24], [29,26], [29,30], [23,24], [23,30], [28,25], [22,22], [29,28], [27,20], [27,22], [29,20], [27,28], [30,24], [28,27], [30,30], [30,29], [28,23], [22,25], [24,24], [25,22], [29,24], [25,23], [27,22], [25,30], [27,28], [23,27], [20,22], [21,30], [22,30], [20,20], [22,20], [24,24], [23,29], [26,23], [28,25], [28,26], [28,23], [20,25], [21,24], [24,29], [20,29], [20,28], [29,28], [30,28], [29,20], [21,21], [28,24], [22,29], [24,23], [25,23], [25,27], [26,22], [28,25], [28,28], [30,23], [25,28], [22,25], [26,24], [20,28], [30,23], [26,21], [23,26], [22,29], [22,30], [27,29], [29,20], [22,30], [27,25], [26,27], [28,21], [25,22], [25,27], [21,22], [20,26], [23,21], [27,26], [25,22], [27,20], [26,20], [23,24], [23,20], [21,25], [28,23], [27,28], [22,25], [25,21], [23,28], [20,25], [29,23], [22,29], [27,30], [30,23], [28,23], [29,20], [28,23], [20,26], [30,26], [23,29], [23,25], [24,26], [28,25], [30,28], [24,26], [29,21], [22,27], [28,23], [24,20], [26,22], [22,27], [22,29], [22,29], [25,26], [22,24], [20,27], [28,30], [28,23], [25,21], [28,26], [29,28], [23,21], [25,27], [25,28], [22,27], [28,23], [30,30], [23,20], [24,29], [28,25], [30,28], [28,23], [27,22], [26,28], [29,25], [23,26], [21,21], [28,29], [20,22], [25,21], [27,21], [23,26], [21,22], [29,20], [20,27], [22,28], [25,21]]


#################this part of code is to fill a file with info that can be copied and pasted 
############ to our sec1 variable ( slight changes are to be made for sec2) to have enough data to work on

#f = open('newstest.txt', 'w+')
#for i in range(500):
#    n = random.randint(0,10)
#    m = random.randint(0,10)
#    if sqrt(m**2+n**2)<10 :
#        sec1.append([m,n])
#        mm=str(m)
#        nn=str(n)
#        f.write("[" + mm + "," + nn + "], ")
#f.close()

radius=0
ourx=input("enter the new point (x, y): \nx: ")
oury=input("y: ")
ourxx= int(ourx)
ouryy= int(oury)
k=5                 #this is the parameter k that we chose
ourk=0
tosec1=0
tosec2=0
while ourk<k:
    radius=radius+0.1
    ourk=0
    tosec1=0
    tosec2=0
    for i in range(165):
        if i<81:
            distance1=sqrt((ourxx-sec1[i][0])**2+(ouryy-sec1[i][1])**2)
            if (distance1<=radius):
                ourk=ourk+1
                tosec1=tosec1+1

        distance2=sqrt((ourxx-sec2[i][0])**2+(ouryy-sec2[i][1])**2)
        if (distance2<=radius):
            ourk=ourk+1
            tosec2=tosec2+1


if tosec1>tosec2 :
    print(str(ourxx)+ ","+ str(ouryy)+" is closest to the inner circle")
    co="red"

else:
    print(str(ourxx)+ ","+ str(ouryy)+" is closest to the outer circle")
    co="blue"


for po in ss1:
    plt.scatter(po[0], po[1], c="red")
for po in ss2:
    plt.scatter(po[0],po[1], c="blue")

plt.scatter(ourxx,ouryy, c=co)
plt.show()
    

