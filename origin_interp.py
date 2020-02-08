#!/usr/bin/py 

import numpy

# input section 

temp1 = input('zadaj DOLNU hranicu TEPLOTY: ')
print('--------------------------------------')
temp2 = input('zadaj HORNU hranicu TEPLOTY: ')
print('--------------------------------------')

xp =(int(temp1), int(temp2))


cp1 = input('zadaj DOLNU hranicu integr KAPACITY: ')
print('--------------------------------------')
cp2 = input('zadaj HORNU hranicu integr KAPACITY: ')
print('--------------------------------------')

fp =(int(cp1), int(cp2))


#interpolation execution 

fl = []

for x in numpy.arange(xp[0],xp[1],0.01):                #ak som to mala cez 'klasicky' range, posledny argument (krok) som nevedela zadat '0.01' lebo papuloval, ze musi byt integer
    n = numpy.interp(x,xp,fp)
    if n <= 4700.00 and n > 4699.97:                    #tu ak som podmienku zadala, ze 'n > 4699', vypisal prazdny zoznam. teraz je to vzhladom na krokovanie premennej 'x' najpresnejsie co viem dostat 
        fl.append(int(x))                               #toto nema vplyv na presnost, len oholi vystup, aby tam nesekal bzilion desatinnych miest 
        fl.append(round(n,2))                           #toto nema vplyv na presnost, len oholi vystup, aby tam nesekal bzilion desatinnych miest 
        #print(fl)                                      #vypise vystup ako zoznam
        print(int(x), "%.2f" % n)                       #vypise vystup ako cisty text
        
