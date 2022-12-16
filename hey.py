#v = 5.0m/s   t=3.0m/s

# Konstanter
v=5.0
t=0
t_slutt=3.0
s=0

dt=0.1
while t<=t_slutt:
    s+=v*dt
    t+=dt
print(s)






