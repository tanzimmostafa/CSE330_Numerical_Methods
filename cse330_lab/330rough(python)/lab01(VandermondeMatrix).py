import numpy as np
import matplotlib.pyplot as plt

#polynomial class
class Polynomial:
    #constructor
    def __init__(self,coeff):
        self.coefficients=coeff
        self.order=len(coeff)-1
        
    #constructor to make the object callable
    #x is the array of which y values we wanna find
    def __call__(self,x):
        res=0
        
        for i in range(self.order+1):
            ai=self.coefficients[i]
            res+=ai*(x**i)
        
        return res
        #res is an array of the corresponding y values
    
    def __repr__(self):
        str=\
        f"{self.order}th order polynomial\
        with coefficients - {self.coefficients}"
        return str
    
    #custom method 1:
    def degree(self):
        return self.order
    
    def coeffs(self):
        return self.coefficients
    

def get_poly(x,y):
        length=len(x)
        X=np.zeros((length,length))
        
        for i in range(length):
            for j in range(length):
                X[i,j]=x[i]**j
                
        X_inv=np.linalg.pinv(X)
        a=np.dot(X_inv,y)
        p=Polynomial(a)
        
        return p
        #object of polynomial class  
        #is returned      
                
                
x = np.array([-3., -2., -1., 0., 1., 3.])
y = np.array([-80., -13., 6., 1., 5., 16.])
P=get_poly(x,y)  

new_x=np.linspace(-3,3,100)
new_y=P(new_x)
              
plt.plot(new_x,new_y,'b-')
plt.plot(x,y,'rx')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['interpolated','nodes'],loc='upper left')
plt.show()


        
        
        
        
        