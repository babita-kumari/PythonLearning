"""
Print all the prime no from 1 to 100

Steps-1:
    Take a list of 1 to 100 numbers & start iteration
    take number = i

Step-2:
    Check if number is divided by any in range of (2, number)
        if it is divided by any then
            no prime
        else
            prime
"""

prime_nos = []
for number in range(1,100):
    prime = 0
    div_count = 0
    for j in range(2, number):
        if (number % j) == 0:
            break;
    else:
        prime_nos.append(number)

print(prime_nos)







