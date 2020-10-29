from datetime import datetime
import numpy as np

n=50
m=100
l=2000
np.random.seed(0)
A=np.random.randint(0,10,((n,m)))
np.random.seed(1)
B=np.random.randint(0,10,(m,l))
# print("A: ",A)
# print("B: ",B)
C=np.zeros((n,l))
# print(len(A))
# print(B[0][:])
t1=datetime.now()
for i in range(len(A)):
    for j in range(0,len(B[0])):
        for k in range(len(B)):
            C[i][j]+=A[i][k]*B[k][j]
t2=datetime.now()

print("Time in 'seconds.microseconds': ", t2-t1)


        





