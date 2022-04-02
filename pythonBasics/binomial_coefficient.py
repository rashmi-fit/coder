'''
Given two numbers n and r, 
find the value of nCr (binomial coefficient: nCr = (n!) / (r! * (n-r)!))
https://www.youtube.com/watch?v=blXQ4RMwEaQ at 4:07
https://codescracker.com/python/program/python-program-find-ncr-npr.htm#:~:text=import%20math%20print
without using a library
'''

def binomial(n, r):
    ''' Binomial coefficient, nCr, n 
        n! / (r! * (n - r)!)
    '''
    p = 1
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

if __name__ == '__main__':
        #input = raw_input
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
    print(binomial(x, y))
