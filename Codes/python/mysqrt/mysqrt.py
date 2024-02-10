"""
Module to calculate squareroot of a number


"""
tol=1.0e-14

kmax=100
def mysqrt2(x):
    """
    Function to calculate squareroot of a number
    """

    s=1.0
    for k in range(kmax):
        r=s
        s= 0.5 *(s+ (x/s))
         
        e=(s-r)/x
        e=abs(e)
        
        if abs(e) < 1e-14:
           break
    return s   
