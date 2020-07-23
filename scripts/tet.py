import numpy as np
import iterate
import cmath

def tet1(x,y):
    iterated = iterate.iterate(lambda n: pow(x,n),y,10)
    # halftet = 0
    # for i in range(0,halfiter.shape[1]):
    #     halftet +=  halfiter[0,i]

    # quartiter = iterate.iterate(lambda n: pow(x,n),0.25)
    # quartet = 0
    # for i in range(0,quartiter.shape[1]):
    #     quartet +=  quartiter[0,i]
    

    
    # table_x = [0,0.25,0.5,1,2]
    # table_y = [1,quartet,halftet,x,pow(x,x)]

    # poly = np.polyfit(table_x,table_y,10)
    # result = np.polyval(poly,y)


    # return result
    
    return np.polyval(iterated,1)


def tet(x,y):
    if y < 0:
        return math.log(tet(x,y+1))/math.log(x)
    elif y >= 0 and y < 1:
        return tet1(x,y)
    else:
        return pow(x,tet(x,y-1))

