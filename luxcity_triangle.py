# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:50:46 2021

@author: shane
"""
"""a function take a number and return a list of strings that, if printed, 
would create a pyramid made of asteriks. 

Created in response to challenge for luxcity game
"""


def triangle(n): 
    #var for use in inner loops
    k=n
    #list to hold results
    strlist=[]
    # outer loop to handle number of rows 
    for i in range(0, n): 
        #establishing container var
        thisstr=''
        #adding requisite amount of spaces
        for j in range(0, k): 
            thisstr=thisstr+' '
        #adding requisite amount of stars
        for j in range(0, i*2+1): 
            thisstr=thisstr+"*"
        #adding requisite amount of spaces
        for j in range(0, k): 
            thisstr=thisstr+' '
        #decrementing for next run
        k = k - 1
        #adding to list
        strlist.append(thisstr) 
    return(strlist)