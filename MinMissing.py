'''
Created on Feb 23, 2017

@author: Daniel
'''
# another just for fun testbut now I want this on a seperate branch, lets see!?
import itertools

def solution(A):
    ls =list(itertools.permutations(A,3))
    for arra in ls:
        if(arra[0]+arra[1]>arra[2] and arra[1]+arra[2]>arra[0] and arra[2]+arra[0]>arra[1]):
            return 1
    return 0
        
        
        
    

    
    

   
arr =[-10,2,5,1,8,20] 
print(solution(arr))