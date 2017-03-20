'''
Created on Feb 11, 2017

@author: Daniel
'''

#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    temp=data
    nonunique=[]
    
    for x in range(0,len(data)):
        count = 0
        #print("we are looking at the: " + str(x) + " element with a value of : " + str(data[x]))
        for y in range(0,len(temp)):
            if(data[x]==temp[y]):
                count = count +1
                #print(str(count) + " instances of the value " + str(data[x]))
                if(count==2):
                    nonunique.append(data[x])
    return nonunique

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"