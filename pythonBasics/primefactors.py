# Task: Write a Python function that does the prime factorization of any number.
# Input: Integer
# Output: List of Prime Factors
# Example: Input - 12 , Output - [2, 2, 3]

def prime_fact(x):
    prime_factors=[]
    divisor=2
    while divisor<=x:
        if x%divisor==0:
            prime_factors.append(divisor)
            x=x/divisor
        else: 
            divisor +=1
    return prime_factors

print(prime_fact(12))
print(prime_fact(630))

