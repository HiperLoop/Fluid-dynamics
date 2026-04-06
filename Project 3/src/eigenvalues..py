import numpy as np
import cmath
import matplotlib.pyplot as plt

def update_values0(M,r): 
    """This function updates the matrix M for the equilibrium state (X0, Y0, Z0) = (0,0,0)"""
    X0=0
    Y0=0
    Z0=0
    M=np.array([[-s, s, 0],[r-Z0, -1, -X0],[Y0, X0, -b]])
    return(M)

def update_values1(M,r): 
    """This function updates the matrix M for the state (X0, Y0, Z0) = (sqrt(b*(r-1)), sqrt(b*(r-1)), r-1)"""
    X0=np.real(cmath.sqrt(b*(r-1))) #Using cmath to find imaginary numbers when r<1, but taking the real part since we are looking for the highest real eigenvalue
    Y0=np.real(cmath.sqrt(b*(r-1)))
    Z0=r-1
    M=np.array([[-s, s, 0],[r-Z0, -1, -X0],[Y0, X0, -b]])
    return(M)
def update_values2(M,r): 
    """This function updates the matrix M for the state (X0, Y0, Z0) = (-sqrt(b*(r-1)), -sqrt(b*(r-1)), r-1)"""
    X0=np.real(-cmath.sqrt(b*(r-1)))
    Y0=np.real(-cmath.sqrt(b*(r-1)))
    Z0=r-1
    M=np.array([[-s, s, 0],[r-Z0, -1, -X0],[Y0, X0, -b]])
    return(M)

def main():
    """This is the main function to run the code for part c) of the analytical part. Change between the equilibrium states in the line below"""
    update_function=update_values2 #Change between the three equilibrium states here by changing the update function between 0,1, and 2
    
    a=np.arange(0.1, 100.1, 0.1) #Array size to determine for which r values to compute the eigenvalues
    M=np.zeros((3,3)) #Initialise the matrix M
    N=[] #Initialise N to store the maximum eigenvalues for each r
    for r in a:
        M = update_function(M,r)
        N.append(np.max(np.linalg.eigvals(M)))
    plt.plot(a, N)
    plt.xlabel('r')
    plt.ylabel('Max Eigenvalue')
    plt.title('Max Eigenvalue vs r')
    plt.grid()
    plt.show()
    print(np.linalg.eigvals(M))
    print(np.linalg.eig(M))
#Define global constants
s=10 
b=8/3

main()