'''
Created on Feb 11, 2017

@author: Daniel
'''

def checkio(data):
    Letters = ["M","D","C","L","X","V","I"]
    Numbers = [1000,500,100,50,10,5,1]
    Roman =""
    
    for x in range(0,len(Numbers)):
        if((data % Numbers[x])== data):
            continue
        else:
            diff =0
            diff = data - (data % Numbers[x])
            print(diff) 
            data = data % Numbers[x]
            print(data)
            count= diff/Numbers[x]
            print(count)
            while(count):
                Roman=Roman+Letters[x]
                print(Roman)
                count = count-1
            
            
    #replace this for solution
    return Roman

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(6) == 'VI', '6'
    #assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    #assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'