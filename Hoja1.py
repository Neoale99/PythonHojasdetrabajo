def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:A
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('Escribe un numero: '))
    result = isPrime(num)

    if result is True:
        print('Es primo')
    else:
        print('El numero no es primo')

if __name__ == '__main__':
    app()