# -*- coding: utf-8 -*-

"""
Created on 12/01/2022
@author: Nagesh

Input file format:
q:5 r:2 s:7
q:3 r:5 s:6

Output:
"q":5, "r":2, "s":7
"""

import sys
import os

def main():
    args = sys.argv[1:]
    if len(args)>1 or len(args)<1:
        print("Error: Takes only one argument")
    else:
        input1 = args[0]
        print(input1)
        print("processing")
        try:
            d = {}
            with open(input1, 'r', encoding = "utf-8") as f:
                for line in f.readlines():
#                    print(line)
#                    l=[line]
#                    print(l)
                    s=[]
                    for i in line.split(" "):
                        s.append(i) #convert strings to list
#                    print(s)
                    d=dict(x.strip().split(":") for x in s) #dictionary comprehension: converting list to dictionary
#                    print(d)
                    e={a: int(x) for a, x in d.items()} #dictionary comprehension: converting the values from string format to integer format
                    print(e)
#                    print(line.strip().split(":"))
        except:
            print("Process failed")
#    print(d)
if __name__ == "__main__":
    sys.exit(main())
