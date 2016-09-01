# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
Avt = []
Anvt = []
Hrt = []
Est = []
Hvt = []
Trt = []
Pst = []

import math
import matplotlib.pyplot as plt
import numpy as np

def logistic(x):
    K=0.9
    return 2/(1+math.exp(-K*x))-1

roundCounter = 0
roundMax = 25

Tr = [1, 1, 1, 1]
Hv = [0, 0, 0, 0, 0, 0, 0, 0]

SAv = [(0,5), (1,1), (0,5), (1,1), (0,4), (1,2), (0,1), (1,5)]
S = [0, 1]
Ps = [0,0]
Es = [1, 1]
Vr = {0:{1:(Hv[1],SAv[1]), 0:(Hv[0],SAv[0])}, \
    1:{3:(Hv[3],SAv[3]), 2:(Hv[2],SAv[2])}, \
    2:{5:(Hv[5],SAv[5]), 4:(Hv[4],SAv[4])}, \
    3:{7:(Hv[7],SAv[7]), 6:(Hv[6],SAv[6])} }
R = {1:(Tr[1],Vr[1]), 2:(Tr[2],Vr[2]), 3:(Tr[3],Vr[3]), 0:(Tr[0],Vr[0])}

Nv = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],0:[]}
Dv = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],0:[]}

for r in Vr.keys():
    vsa = Vr[r]
    for v in vsa.keys():        
        s,a = vsa[v][1][0], vsa[v][1][1]        
        for r2 in Vr.keys():
            wsa = Vr[r2]
            for w in wsa.keys():
                if v!=w:
                    if s==wsa[w][1][0]:
                        if abs(a-wsa[w][1][1])<=1:
                            Nv[v].append(w)
                        else: Dv[v].append(w)

V2R = {}                        
for r in Vr.keys():
    vsa = Vr[r]
    for v in vsa.keys():
        V2R[v] = r
        
Av = {}
Anv = {}            
for r in Vr.keys():
    #print("r:",r
    vsa = Vr[r]
    #print("Vr[r]:",vsa
    for v in vsa.keys():
        for n in Nv[v]:
            if Av.get(v,0):
                Av[v] += Tr[V2R[n]]
            else: Av[v] = Tr[V2R[n]]
        for n in Dv[v]:
            if Av.get(v,0):
                Av[v] -= Tr[V2R[n]]
            else: Av[v] = -Tr[V2R[n]]

for v in Av.keys():
    Anv[v] = logistic(Av[v])
    

    

Avt.append(Av.items())
Anvt.append(Anv.items())
      
                    
for roundCounter in range(roundMax):
    print ("COUNTER = ",roundCounter)
    
    for r in Vr.keys():
        print ("Hv Calculation r:",r)
        vsa = Vr[r]
        print ("Vr[r]:",vsa)
        for v in vsa.keys():
            print ("- v:",v)        
            h,s,a = vsa[v][0], vsa[v][1][0], vsa[v][1][1]
            
            Hv[v] = abs(Es[s])*Anv[v]
            SAv[v] = (s,a)
            Vr[r][v] = (Hv[v], SAv[v])
            print ("- h s a  Vr[r][v] : ",h,s,a,Vr[r][v])
    
    Hr = [0,0,0,0]
    for r in Vr.keys():
        print ("Trust Calculation r:",r)
        vsa = Vr[r]
        print ("Vr[r]:",vsa)
        for v in vsa.keys():
            print ("- v:",v)        
            h,s,a = vsa[v][0], vsa[v][1][0], vsa[v][1][1]
            Hr[r] += h
            print ("- Hr[%s] += %s:" %(r,h))
        Tr[r] = logistic(Hr[r])
        print ("r=%s, Hr[r], Tr[r] : %s, %s" %(r,Hr[r],Tr[r]))
    
   
    for r in Vr.keys():
        print("Es Calculation r:",r)
        vsa = Vr[r]
        print("Vr[r]:",vsa)
        for v in vsa.keys():
            print("- v:",v)        
            h,s,a = vsa[v][0], vsa[v][1][0], vsa[v][1][1]
            print("- h s a : ",h, s,a)
            if Tr[r] > 0:
                print("- - Tr:",Tr[r])
                Ps[s] += Tr[r]*(a-3)
                print("- - Ps+=:" , Tr[r]*(a-3))
     
    for p in range(len(Ps)):
        Es[p] = logistic(Ps[p])
    print("Ps, Es :",Ps,Es)
        
        
    Av = {}
    Anv = {}            
    for r in Vr.keys():
        vsa = Vr[r]
        print("Av calculation r=%s, Vr[r]=%s:" %(r,vsa))
        for v in vsa.keys():
            for n in Nv[v]:
                if Av.get(v,0):
                    Av[v] += Tr[V2R[n]]   # n's reviewer's trust *******************
                    print("- Av[%s] += %s=Tr[%s]" %(v,Tr[V2R[n]],V2R[n]))
                else:
                    Av[v] = Tr[V2R[n]]
                    print("- Av[%s] = %s=Tr[%s]" %(v,Tr[V2R[n]],V2R[n]))
            for n in Dv[v]:
                if Av.get(v,0):
                    Av[v] -= Tr[V2R[n]]
                    print("- Av[%s] -= %s=Tr[%s]" %(v,Tr[V2R[n]],V2R[n]))
                else:
                    Av[v] = -Tr[V2R[n]]
                    print("- Av[%s] = -%s= -Tr[%s]" %(v,Tr[V2R[n]],V2R[n]))
                
    
    for v in Av.keys():
        Anv[v] = logistic(Av[v])
    print("Av, Anv",Av,Anv)
        
    Avt.append(Av.items())
    Anvt.append(Anv.items())
    Pst.append(list(Ps))            
    Hvt.append(list(Hv))        
    Est.append(list(Es))      
    Hrt.append(list(Hr))
    Trt.append(list(Tr))

values0 =  [elem[0] for elem in Trt] 
values1 =  [elem[3] for elem in Trt]
hist = range(1,roundMax+1)
plt.figure()
plt.plot(hist, values0,'go-') 
plt.plot(hist, values1,'rs-') 
plt.legend(['Reviewer 0,1,2', 'Reviewer 3'])
plt.xlabel('Iteration')
plt.ylabel('Trustiness T(r)')
plt.title('Iterative Calculation of Trustiness')
plt.show()
plt.close()

values0 =  [elem[0] for elem in Hvt] 
values1 =  [elem[6] for elem in Hvt]
hist = range(1,roundMax+1)
plt.figure()
plt.plot(hist, values0,'go-') 
plt.plot(hist, values1,'rs-') 
plt.legend(['Reviews 0..5', 'Reviews 6,7'])
plt.xlabel('Iteration')
plt.ylabel('Honesty H(v)')
plt.title('Iterative Calculation of Honesty')
plt.show()
plt.close()

values0 =  [elem[0] for elem in Est] 
values1 =  [elem[1] for elem in Est]
hist = range(1,roundMax+1)
plt.figure()
plt.plot(hist, values0,'go-') 
plt.plot(hist, values1,'rs-') 
plt.legend(['Store 0', 'Store 1'])
plt.xlabel('Iteration')
plt.ylabel('Reliability H(r)')
plt.title('Iterative Calculation of Reliability')
plt.show()
plt.close()

values0 =  [list(elem)[0][1] for elem in Anvt] 
values1 =  [list(elem)[6][1] for elem in Anvt]
hist = range(0,roundMax+1)
plt.figure()
plt.plot(hist, values0,'go-') 
plt.plot(hist, values1,'rs-') 
plt.legend(['Review 0..5', 'Review 6,7'])
plt.xlabel('Iteration')
plt.ylabel('Agreement(v)')
plt.title('Iterative Calculation of Agreement')
plt.show()
plt.close()


        
