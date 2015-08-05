from math import factorial
import sys


def getZerosFactorial(number):
    '''
    Obtiene la cantidad de ceros del factorial de 'number'
    Args:
    - Number: Numero al cual se desea obtener el la cantidad de 0's de su factorial.
    Return:
    - Cantidad de 0's del factorial de number
    '''
    n=factorial(number)
    count=0
    while n > 10:
        mod=n%10
        if mod == 0:
            count+=1
        n=long(n/10)
    return count

if __name__ == '__main__':
    n=int(sys.argv[1])
    print "Factorial %i" % factorial(n)
    print "Ceros:%i" % getZerosFactorial(n)
