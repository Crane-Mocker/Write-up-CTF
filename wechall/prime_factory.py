#!/usr/bin/python3
import math

#if is prime
def isPrime(num):
    if(num <= 3):
#        print("it is prime")
        return True
    else:
        for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0:
#                print("it is not prime")
                return False
#        print("it is prime")
        return True

#if the separate digit sums are also prime
def sumIsPrime(num):
    sum = 0
    while num >= 1:
        sum += num % 10
        num = int(num / 10)
#    print("The sum:" + str(sum))
    return isPrime(sum)

def searchForNum():
    num = 1000001
    count_num = 0
    while count_num < 2:
#        print("The num is:" + str(num))
        if(sumIsPrime(num)):
            if(isPrime(num)):
                count_num += 1
                print("one result is:" + str(num))
        num += 2

print(searchForNum())
