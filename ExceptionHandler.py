'''
Created on Mar 15, 2017

@author: Daniel
'''

if __name__ == '__main__':
    print("Does this run auto")
    list = []
    list.append("Daniel")
    list.append([1])

    print(list[0])
    print(list[1])
    #print(list[3])
    try:
        print(list[3])
    except IndexError:
        print("sorry bruh, out of index")
        