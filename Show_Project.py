# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:37:35 2020

@author: ccsuc
"""

import timeit
import pandas as pd
import numpy as np
from functools import reduce
from itertools import combinations

df_com = pd.read_excel("C:/Users/ccsuc/Desktop/Personal_Projects/Show_Project_Folder/Community_Cast.xlsx")
df_par = pd.read_excel("C:/Users/ccsuc/Desktop/Personal_Projects/Show_Project_Folder/Parks_And_Rec_Cast.xlsx")
df_off = pd.read_excel("C:/Users/ccsuc/Desktop/Personal_Projects/Show_Project_Folder/Office_Cast.xlsx")
df_roc = pd.read_excel("C:/Users/ccsuc/Desktop/Personal_Projects/Show_Project_Folder/30_Rock_Cast.xlsx")

data = [df_com["Name"], df_par["Name"], df_off["Name"], df_roc["Name"]]
headers = ["Community Names", "ParksAndRec Names", "Office Names", "30 Rock Names"]
df = pd.concat(data, axis=1, keys=headers)

def cleaningAndListing(df):
    cast_list = []
    com_list = df["Community Names"].dropna().to_list()
    par_list = df["ParksAndRec Names"].dropna().to_list()
    off_list = df["Office Names"].dropna().to_list()
    roc_list = df["30 Rock Names"].dropna().to_list()
    cast_list.extend([com_list, par_list, off_list, roc_list])
    return cast_list
    
def twoCombo(arr):
    return list(combinations(arr, 2))

def threeCombo(arr):
    return list(combinations(arr, 3))

showNames = ["Community", "Parks and Rec", "The Office", "30 Rock"]

# We need combos of both the actors and show names to match the two after processing
masterList = cleaningAndListing(df)
twoComboList = twoCombo(masterList)
threeComboList = threeCombo(masterList)
twoComboShows = twoCombo(showNames)
threeComboShows = threeCombo(showNames)

def twoComparisons(arr):
    twoComparisonList = []
    for i in arr:
        twoInCommon = list(set(i[0]) & set(i[1]))
        numInCommon = len(twoInCommon)
        
        
        
twoComparisons(twoComboList)

'''
# Timing section for combinations of length 2. Itertools is faster by far
# Be sure to comment out statments and setups if test again.

a = ['a','b','c','d']
stmt1 = 
arr = ['a','b','c','d']
def twoPair(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            currentPair = []
            currentPair.append(arr[i])
            currentPair.append(arr[j])
            pairs.append(currentPair)
            j+=1
        i+=1
    return pairs
twoPair(arr)

stmt2 = 
arr = ['a','b','c','d']
def itertools(arr):
    combo = list(combinations(arr, 2))
    return combo
itertools(arr)

setup2 = "from itertools import combinations"

print("The time to compute using twoPair is: ", 
      timeit.timeit(stmt = stmt1, number = 10000))

print("The time to compute itertools is: ", 
      timeit.timeit(setup = setup2, stmt = stmt2, number = 10000))


# Timing section. Set semantics are much faster than numpy method
com_list = df_com["Name"].dropna().to_list()
par_list = df_par["Name"].dropna().to_list()
def f():
    list(set(com_list) & set(par_list))

def f1():
    reduce(np.intersect1d, [com_col, par_col])
    
def f2():
    com_list = df_com["Name"].to_list()
    par_list = df_par["Name"].to_list()
    
com_par_common_list = list(set(com_list) & set(par_list))
print("The time to compute using set semantics is: ", 
      timeit.timeit(f, number = 10000) + timeit.timeit(f2, number = 10000))
com_par_common = reduce(np.intersect1d, [com_col, par_col])
print("The time to compute using NumPy is: ", 
      timeit.timeit(f1, number = 10000))
'''
'''
com_off_common = list(set(com_list) & set(off_list))
com_roc_common = list(set(com_list) & set(roc_list))
par_off_common = list(set(par_list) & set(off_list))
par_roc_common = list(set(par_list) & set(roc_list))
off_roc_common = list(set(off_list) & set(roc_list))
com_par_off_common = list((set(set(com_list) & set(par_list))) & set(off_list))
com_off_roc_common = list((set(set(com_list) & set(off_list))) & set(roc_list))
com_par_roc_common = list((set(set(com_list) & set(par_list))) & set(roc_list))
par_off_roc_common = list((set(set(par_list) & set(off_list))) & set(roc_list))
com_par_off_roc_common = list((set((set(set(com_list) & set(par_list))) & set(off_list))) & set(roc_list))
'''
'''
print("For Community: ", len(df_com.index))
print("For Parks and Rec: ", len(df_par.index))
print("For The Office: ", len(df_off.index))
print("For 30 Rock: ", len(df_roc.index))

com_list = df_com["Name"].to_list()
par_list = df_par["Name"].to_list()
off_list = df_off["Name"].to_list()
roc_list = df_roc["Name"].to_list()

com_par_common = list(set(com_list) & set(par_list))
com_off_common = list(set(com_list) & set(off_list))
com_roc_common = list(set(com_list) & set(roc_list))
par_off_common = list(set(par_list) & set(off_list))
par_roc_common = list(set(par_list) & set(roc_list))
off_roc_common = list(set(off_list) & set(roc_list))
com_par_off_common = list((set(set(com_list) & set(par_list))) & set(off_list))
com_off_roc_common = list((set(set(com_list) & set(off_list))) & set(roc_list))
com_par_roc_common = list((set(set(com_list) & set(par_list))) & set(roc_list))
par_off_roc_common = list((set(set(par_list) & set(off_list))) & set(roc_list))
com_par_off_roc_common = list((set((set(set(com_list) & set(par_list))) & set(off_list))) & set(roc_list))

print("Community and Parks and Rec have", len(com_par_common),"actors in common")
print("Community and The Office have", len(com_off_common), "actors in common")
print("Community and 30 Rock have", len(com_roc_common), "actors in common")
print("Parks and Rec and The Office have", len(par_off_common), "actors in common")
print("Parks and Rec and 30 Rock have", len(par_roc_common), "actors in common")
print("The Office and 30 Rock have", len(off_roc_common), "actors in common")
print("Community, Parks and Rec, and The Office have", len(com_par_off_common), "actor in common")
print("Community, The Office, and 30 Rock have",len(com_off_roc_common),"actors in common")
print("Community, Parks and Rec, and 30 Rock have",len(com_par_roc_common),"actor in common")
print("Parks and Rec, The Office, and 30 Rock have",len(par_off_roc_common),"actors in common")
print(com_par_off_common, "was in Community, Parks and Rec, and The Office")
print(com_off_roc_common, "were in Community, The Office, and 30 Rock") 
print(com_par_roc_common, "was in Community, Parks and Recreation, and 30 Rock")
print(par_off_roc_common, "were in Parks and Rec, The Office, and 30 Rock")
print("And finally, the original question:")
print(len(com_par_off_roc_common), "people were in Community, Parks and Rec, The Office, and 30 Rock ")
'''