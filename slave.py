import os
import time

def readLines(file_name):
  f = open(file_name,"r")
  L = f.readlines();
  f.close()
  return L

def writeLines(file_name,L):
  f = open(file_name,"w")
  f.write(''.join(L))
  f.close()
  return L
  


while True:
  try:
    L = readLines("commands.txt")
    if len(L) !=0:
      cmd = L[0].strip()
      L.pop(0)
      writeLines("commands.txt",L)
      print "Executing: "+cmd
      flag = os.system(cmd)
      if flag!=0:
         L = readLines("commands.txt")
         L.append(cmd)
         writeLines("commands.txt",L)
    time.sleep(1)
  except: 
    time.sleep(1)
    pass
