# -*- coding: utf-8-*-
"""
Created on Wed Aug 12 01:13:30 2020

@author: TheThBa
"""

import os.path
import re
from shutil import copyfile

path = "" #MOD DIRECTORY HERE LIKE C:/Users/USER/Documents/Paradox Interactive/Hearts of Iron IV/mod/MODNAME/ <- final slash important!
replace_path_active = 0 #if you are using replace_path on state files, set this to 1, otherwise keep it at 0, otherwise you will get a ton of ID errors 

###############################################################################################

statespath = os.path.join(path, "history/states/")
locpath = os.path.join(path, "localisation/state_names_l_english.yml")
newpath = os.path.join(path, "history/newstates") #<------ where new files are saved

################################################################################################

def copyfilefunc(l,file):
    f = open(l, "r")
    line = f.readline()
    idfound = 0
    id = 0
    if replace_path_active == 0:
        r = os.path.join(newpath, file)
        copyfile(l,r)
        blank = open(r, "w")
        blank.truncate(0)
        blank.write("#blank to avoid ID errors")
        blank.close
    while line and idfound == 0:
        if re.search('id=.+',line) or re.search('id = .+',line):
            id = int(re.findall(r'\d+', line)[0]) #actually outputs 1d 1element array, which is why we select first element
            idfound = 1
            #print(id)
        line = f.readline()
    j = open(locpath, "r", encoding = "utf-8")
    line2 = j.readline()
    idfound = 0
    name = "error"
    while line2 and idfound == 0:
        if re.search('STATE_'+str(id)+':. \".+\"', line2):
            name = re.findall('"([^"]*)"', line2)[0]
            idfound = 1
        line2 = j.readline()
    h = os.path.join(newpath, str(id)+"-"+str(name)+".txt")
    copyfile(l,h)
    f.close
    j.close
statefiles = [f for f in os.listdir(statespath) if os.path.isfile(os.path.join(statespath,f))] #gain array of all files in directory
x = 0
if not os.path.exists(newpath):
    os.mkdir(newpath)

while x < len(statefiles):
    copyfilefunc(os.path.join(statespath,statefiles[x]),statefiles[x])
    x = x+1