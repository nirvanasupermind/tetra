import numpy as np
import math

def constructPoly(f):
     x = np.array([])
     y = np.array([])
     for m in range(-50,50):
        try:
                 #Use a trycatch to dodge MathDomainError
                 if math.isfinite(f(m)):
                    
                    x = np.append(x,m)
                    y = np.append(y,m)
        except:
                 x = x
                 y = y

     print(x)
        
      
     return np.polyfit(x,y,30)

def expfit(x,y):
    newx = x
    newy = np.array([math.log(item) for item in list(y)])
    linear = np.polyfit(newx,newy,1)
    return [math.exp(linear[1]),math.exp(linear[0])]

def constructExp(f):
     x = np.array([])
     y = np.array([])
     for m in range(-50,50):
        try:
                 #Use a trycatch to dodge MathDomainError
                 if math.isfinite(f(m)):
                    
                    x = np.append(x,m)
                    y = np.append(y,f(m))
        except:
                 x = x
                 y = y
        
     return expfit(x,y)

def firstDerivPoly(poly):
    return np.poly1d(poly).deriv().coef

def firstDerivExp(exp):
    return np.array([exp[0]*math.log(exp[1]),exp[1]])

def derivPoly(poly,n):
    result = poly
    for i in range(0,n):
        result = firstDerivPoly(result)
    return result


def derivExp(exp,n):
    result = exp
    for i in range(0,n):
        result = firstDerivExp(result)
    return result


def useExp(f):
    ratios = np.array([])
    for i in range(0,50):
        try: 
            #Use a trycatch to dodge MathDomainError
            if math.isfinite(f(i+1)) and math.isfinite(f(i)):
                ratios = np.append(ratios,f(i+1)/f(i))
        except:
            ratios = ratios
    
    
        
    if np.mean(ratios) - ratios[0] <= 1e-7 and np.mean(ratios) - ratios[len(ratios)-1] <= 1e-7:
        return True
    elif np.amin(ratios) == ratios[len(ratios)-1]:
        return False
    else:
        return True

def deriv(f,x,n):
    if useExp(f):
        return derivExp(constructExp(f),n)[0]*pow(derivExp(constructExp(f),n)[1],x)
    else:
        return np.polyval(derivPoly(constructPoly(f),n),x)

           


