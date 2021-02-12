def triangulo(n):
    return "\n".join(["*"*i for i in range(1,n+1)])
 
numero=int(input("indica un numero: "))
print(triangulo(numero))