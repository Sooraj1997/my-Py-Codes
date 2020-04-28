def staircase(n):
    for i in range(1,n+1):
        sample='#'*i
        print(sample.rjust(n))
n=int(input('Enter number of steps in staircase'))
staircase(n)
