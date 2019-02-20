#Fibonacci3
#Adding tracking information to the fib function
#BY: Ifeatu Okaneme

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    n = int(input("Enter a positive integer: "))
    
    
    for i in list(range(n)):
        print("Computing fib(" , fib(n), ")")
        print("Leaving fib(", fib(n), ") returning ", fib(n-1))    

main()

#use a for loop or while like in class    
