
import os

print(os.getcwd())
# open file in read mode 
fn = open("input.txt", 'r') 
  
# open other file in write mode 
fn1 = open('output.txt', 'w') 
  
# read the content of the file line by line 
cont = fn.readlines() 
print(cont)
print(len(cont))


type(cont) 
for i in range(0, len(cont)): 
    if(i % 2 != 0): 
        fn1.write(cont[i]) 
    else: 
        pass

"""
# close the file 
fn1.close() 
  
# open file in read mode 
fn1 = open('output.txt', 'w+') 
  

# read the content of the file 
cont1 = fn1.read() 
  
# print the content of the file 
print(cont1) 
  
# close all files 
fn.close() 
fn1.close() 

"""
