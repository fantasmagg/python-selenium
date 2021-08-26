def contador(max):
    print("=Dentro de contador - empezando")
    n=0
    while n < max:
        print(f"=Dentro de contador - viene yield con n={n}")
        yield
        print("=Dentro de contador - retomando después de yield")
        n=n+1
    print("=Dentro de contador - terminando")

print("Instanciando contador")
mycont = contador(3)
print("Contador instanciado")

for i in mycont:
    print(f"valor leido del iterador={i}")
print("Listo")