'''
Created on Feb 12, 2017

@author: Daniel
'''
Board = ["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8","c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8","e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8","g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]
def safe_pawns(pawns):
    check = 0
    howmany=0
    paw = pawns
    for x in paw:
        check=check+1
        #print(x)
        use1 = returnlocation(x)-10
        use2 = returnlocation(x)+6
        print(str(x)+ " found at location "+str(use1))
        #if((use1 - 10)<=1|(use2+6)>=64):
        #    use1=1
        #    use2=63
        if(use2+6>65):
            continue
        if(isinarray(Board[use1], paw)| isinarray(Board[use2], paw)):
            howmany=howmany+1
        
        
        
    print(howmany)
    return howmany
    

def isinarray(pawnloc,array):
    print(str(pawnloc))
    #print(array)
    for y in array:
        #print(y)
        if(str(pawnloc) == str(y)):
            print("returning true")
            return True
            break
    return False
        
            
        
    
        
def returnlocation(loc):
    count = 0 
    for x in Board:
        count= count+1
        if(x == loc):
            #print(count)
            return (count)
            
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"]) ==7