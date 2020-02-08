#!/usr/bin/python

'''
To run script, use these arguments:

$ python origin_interp.py --temp-bottom 1 --temp-top 2 --cap-bottom 3 --cap-top 4
'''

import sys
import numpy
import argparse

def calculate(temp_bottom, temp_top, cap_bottom, cap_top):
    xp =(int(temp_bottom), int(temp_top))
    fp =(int(cap_bottom), int(cap_top))

    #interpolation execution

    fl = []

    for x in numpy.arange(xp[0],xp[1],0.01):                #ak som to mala cez 'klasicky' range, posledny argument (krok) som nevedela zadat '0.01' lebo papuloval, ze musi byt integer
        n = numpy.interp(x,xp,fp)
        if n <= 4700.00 and n > 4699.97:                    #tu ak som podmienku zadala, ze 'n > 4699', vypisal prazdny zoznam. teraz je to vzhladom na krokovanie premennej 'x' najpresnejsie co viem dostat
            fl.append(int(x))                               #toto nema vplyv na presnost, len oholi vystup, aby tam nesekal bzilion desatinnych miest
            fl.append(round(n,2))                           #toto nema vplyv na presnost, len oholi vystup, aby tam nesekal bzilion desatinnych miest
            #print(fl)                                      #vypise vystup ako zoznam
            print(int(x), "%.2f" % n)                       #vypise vystup ako cisty text

def main():
    # Quick arguments creation
    parser = argparse.ArgumentParser(description='Script to do magic')
    parser.add_argument("--temp-bottom", help="Bottom temperature boundary", required=True)
    parser.add_argument("--temp-top", help="Top temperature boundary", required=True)
    parser.add_argument("--cap-bottom", help="Bottom capacity boundary", required=True)
    parser.add_argument("--cap-top", help="Top capacity boundary", required=True)
    args = parser.parse_args()

    print(args.cap_top)
    calculate(args.temp_bottom, args.temp_top, args.cap_bottom, args.cap_top)

if __name__ == "__main__":
    sys.exit(1) if not main() else sys.exit(0)
