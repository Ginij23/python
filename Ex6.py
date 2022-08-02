#fibonacci sereies

def fibonacci_series(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

numbers=int(input("Enter Number for fibonacci series"))
print(fibonacci_series(numbers))
