'''
Created on Feb 23, 2017

@author: Daniel
'''




#Dont care too much , Just want to see that local changes can effect the GitRepo

def solution(A):
    #print(X)
    #print(A)
    
    
    #print(sorted)
    boolarr = [False]*len(A)
    #print(boolarr)
    limit = len(A)
    
    for value in A:
        if((value>limit) or (value<=0)):
            return 0
        elif(boolarr[value-1]==True):
            return 0
        else:
            boolarr[value-1]=True
    return 1
            
        
    #print(sorted[5])
    
        
    
    
    
    
#     start = np.searchsorted(a, 6, 'left')
#     end = np.searchsorted(a, 10, 'right')
#     rng = np.arange(start, end)
#     rng
#     
    
    

    
    

   
arr =[4,1,3,2] 
print(solution(arr))