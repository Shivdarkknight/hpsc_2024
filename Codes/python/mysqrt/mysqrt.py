x= 2.0
s= 1.0
kmax= 20
for k in range(kmax):
    r=s
    s= 0.5 *(s+ (x/s))
    e=(s-r)/x
    print(s)
    if abs(e) < 1e-04:
     break
