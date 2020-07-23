import numpy as np
import deriv
import math

def fac(x):
    #Q&D recursive factorial for carlemanmatrix
    if x == 0:
        return 1
    else:
        return x*fac(x-1)

def sqrtm(a):
    #Finds the square root of np matrix
    y = a
    z = np.matrix(np.identity(a.shape[0]))
    #Perform Denman-Beaver iteration w/ 500 terms
    for i in range(0,500):
        y_old = y
        z_old = z
        # print('*****z_old='+str(z_old)+'|i='+str(i))
        # print('*****y_old='+str(y_old)+'|i='+str(i))
        y = (y_old+z_old.I)*0.5
        z = (z_old+y_old.I)*0.5
    
    
    
    return y



def getCarleman(f,size):
    #Gets the carlemanmatrix of a function
    result = []
    for m in range(0,size):
        result.append([])
        for n in range(0,size):
            result[m].append(deriv.deriv(lambda x: pow(f(x),m),0,n)/fac(n))
    return np.matrix(result)


def zeroIterate(f,size):
    return np.matrix(np.identity(size))[1,:]

def halfIterate(f,size):
    return sqrtm(getCarleman(f,size))[1,:]



def quarterIterate(f,s):
    return sqrtm(sqrtm(getCarleman(f,size)))[1,:]

def oneIterate(f,s):
    return getCarleman(f,size)[1,:]



def collectIterPoly(f,index,size):
    
    table_x = [0,0.25,0.5,1]
    table_y = [
        zeroIterate(f,size)[0,index],
        quarterIterate(f,size)[0,index],
        halfIterate(f,size)[0,index],
        oneIterate(f,size)[0,index]
    ]


    

    return np.polyfit(table_x,table_y,size)

def iterate(f,n,size):
    result = np.array([])
    for i in range(0,5):
        result = np.append(result,np.polyval(collectIterPoly(f,i,size),n,size))

    return result

    

    
        
        
        

    

# def gcd(a, b):
#     #Find gcd for simplification of fraction
#     while b:
#         a, b = b, a % b
#     return a

# def simplify(a,b):
#     return (a/gcd(a,b),b/gcd(a,b))

# def nearestBinFrac(x):
#     return simplify(math.floor(64*x),64)

# def powm(a,x):
#     binf = nearestBinFrac(x)
#     result = np.matrix(np.identity(a.shape[1]))
#     result_old = result
#     for i in range(0,math.floor(binf[0])):

#         result = binaryRootm(a,int(round((math.log(binf[1]/math.log(2))))))*result
    
#     return result



# def iterate(f,n):
#     return powm(getCarleman(f,5),n)[1]

