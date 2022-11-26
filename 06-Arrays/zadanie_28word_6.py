import math

def median( theSeq ):
    n = len( theSeq )

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n - 1) :
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    if len(theSeq)%2 != 0:
        x=len(theSeq)//2
        return theSeq[x]
    else:
        x=(len(theSeq)//2)+math.ceil(len(theSeq)/2)
        return x/2