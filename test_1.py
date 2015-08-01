from math import factorial

def getTrailingZeros(number):
    """
    Obtiene la cantidad de ceros que tiene el factorial de 'number', basandose en el numero de multiplos de 5, menores a 'number'
    Vease:
    - http://www.ganitcharcha.com/view-article-A-Note-on-Factorial-and-it%27s-Trailing-Zeros.html
    - http://www.purplemath.com/modules/factzero.htm
    """
    count = 0
    for i in range(0,number): #Iteramos hasta number
        if i % 5 == 0: #Si el numero actual es multiplo de 5, se incrementa el contador
            count=count+1
    return count


if __name__ == '__main__':
    n=10
    print "Factorial:%i" % factorial(n)
    print "Cantidad de ceros:%d" % getTrailingZeros(n)
