import numpy as np

M=5
N=10
A = np.random.randint(0,10,(N,M))
B = np.random.randint(5,50,(M,2))

weights_and_revenue = A.dot(B)
print(A)
print()
print(B)
print()
print(weights_and_revenue)

is_less_than_500 = weights_and_revenue[:,1] < 500

print(weights_and_revenue[is_less_than_500,1].argmax() )


















