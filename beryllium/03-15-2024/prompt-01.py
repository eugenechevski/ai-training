def modelA():
    def factorial(n):
        if n == 0:
            return 1
        else:
            result = 1
            for i in range(2, n+1):
                result = result * i
            return result
        
    print(factorial(6))

    
def modelB():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n+1):
                result *= i
            return result

    print(factorial(5))  # Output: 120
    print(factorial(10)) # Output: 3,628,800
    print(factorial(20)) # Output: 2,432,902,008,176,640,000
    
    
print("Model A")
modelA()
print()

print("Model B")
modelB()
print()