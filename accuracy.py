from __future__ import barry_as_FLUFL
from asyncore import read
import readline

from cmath import inf
import copy
pred = open('data/pred.txt','r')
init = open ('input1.txt'  , 'r')
tgt = open('data/corpusz.txt','r')
j = 0 
totalsent = 0  
net = 0 
while pred:

    
    score = 0
    prevscore  = 0 
    total = 0 
    f1 = pred.readline()
    f2 = tgt.readline()
    f3 = init.readline()
    f1 = f1.split()
    f2 = f2.split()
    f3 = f3.split()
    if len(f1) == 0 :
        break
    j += 1 
    totalsent+= 1

    for i in range(len(f1)):
        if f1[i] == f2[i]:
            score+= 1
        if f3[i] == f2[i] :
            prevscore += 1 
        # else :
            # print(f1[i] , f2[i])
        total += 1
    
    print(f'Initial score = {(prevscore/total)*100},  final score = {(score/total)*100}% , sentence number {j}' )

    net += ((score/total)*100)

print(f'average final acc = {net / totalsent}')



