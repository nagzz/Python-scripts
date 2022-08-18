# -*- coding: utf-8 -*-
"""
Created on 27/01/22

@author: Nagesh
"""
import sys
import os
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import StrMethodFormatter
from matplotlib.pyplot import figure

def main():
    args = sys.argv[1:]
    if len(args)>4 or len(args)<4:
        print("Error: takes only four arguments")
    else:
        df= pd.read_csv(args[0])
        color=args[2]
        print(df)
        row_index = df.index
        print(row_index)
        x = np.array(row_index)
        print(x)
        y=df.iloc[:,1]
        print(y)
        my_xticks = df.iloc[:,0]
        print(my_xticks)
        z = df.iloc[:,2]
        figure(figsize = (8, 6), dpi = 300)
        plt.xticks(x, my_xticks)
        plt.plot(x, y, color='k')
        plt.fill_between(x, y-z,y+z, alpha=0.35, color=color)
#        plt.axhline(y=0, color='k', linewidth=0.5, linestyle = '--')
#        plt.rcParams["font.size"] = "100"
#        matplotlib.rc('xtick', labelsize=20)
        plt.yticks(fontsize=18)#, rotation=180)
        plt.xticks(fontsize=18)
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
#        plt.box(False)
        plt.margins(x=0, tight=True)
        plt.gca().spines['right'].set_color('none')
        plt.gca().spines['top'].set_color('none')
        plt.suptitle(args[3], y=0.9, size=25)
        plt.ylabel('Log2 Fold Change expression', size=20)#, labelpad=0.5)
        plt.xlabel('Infection time point #hpi', size=20)
        plt.savefig(args[1], dpi=300)
"""     
        y=df['miR395a']
        my_xticks = df['ID']
        plt.xticks(x, my_xticks)
        plt.plot(x, y)
        plt.fill_between(x, y-df.Sd,y+df.Sd, alpha=0.35)
        plt.axhline(y=0, color='k')
        plt.savefig('mir395a.png')
"""
if __name__ == "__main__":
    sys.exit(main())
