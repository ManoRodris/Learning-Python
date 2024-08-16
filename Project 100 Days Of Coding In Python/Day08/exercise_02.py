def prime_checker(number):
    number_prime_checker = True
    for i in range(2, number):
        if number % i == 0:
            number_prime_checker = False
    if number_prime_checker:
        print(f"{number} is a prime number")
    else:
        print(f"{number} isn't a prime number")
    
n = int(input()) 
prime_checker(number=n)


