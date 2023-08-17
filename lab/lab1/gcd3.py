# Euclidean algo O(log(max(m,n)))

# if m > n, then GCD(m, n) = GCD(m %n, n) = GCD(m, m %n)
# if m = n, then GCD(m, n) = m = n
# if m< n, thenGCD(m, n) = GCD(m, n %m) = GCD(n %m, n)

import time

def FindGCD3(m : int, n : int) -> int :
    if(m == 0 and n == 0):
        return 0
    if ( m == 0 or n == 0):
        return max(m,n)
    if m > n: 
        return FindGCD3(m % n, n)
    elif m < n:
        return FindGCD3(m , n % m )
    else:
        return m 
    
    
m = 2153599
n = 391675650
start_time = time.perf_counter()
result = FindGCD3(m, n)
end_time = time.perf_counter()

print(f"The GCD of {m} and {n} is {result}")
print(f"Time taken: {(end_time - start_time) *1000} milliseconds")