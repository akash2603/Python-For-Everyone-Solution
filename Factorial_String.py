# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 16:31:29 2017

@author: Akash
"""

def main():
    n = (input("Enter a number: "))
    print(fact(n))
    
def fact(n):
    if n == 0:
        return 1
    else:
        return str(n)+"*"+str(fact(n-1))

main()
        

   




    
    
