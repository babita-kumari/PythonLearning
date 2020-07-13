"""
Count the number of prime numbers less than a non-negative number, n.

solution:
step 1: identify prime number first till n
step 2: count numbers that are prime
"""
import math
class Solution:

    def isPrime(self, number):
        if (number<=1):
            return False
        if (number<=3):
            return True
        if (number%2==0 or number%3==0):
            return False
        sqrt=math.sqrt(number)
        if int(sqrt+0.5)**2==number:
            return False
        i=5
        while(i*i<=number):
            if (number%i==0 or number%(i+2)==0):
                return False
            i=i+6
        return True

    def countPrimes(self,n):
        count=0
        for number in range(1,n):
            if self.isPrime(number)==True:
                count=count+1
        return count

object=Solution()
print(object.countPrimes(100000000))