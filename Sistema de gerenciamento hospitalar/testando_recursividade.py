def fatorial_recursivo(num):
    if num == 1:
        return 1
    else:
        return num * fatorial_recursivo(num - 1)
        
print(fatorial_recursivo(6))

def fibonacci_recursivo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci_recursivo(num - 1) + fibonacci_recursivo(num - 2)
    
print(fibonacci_recursivo(3))

