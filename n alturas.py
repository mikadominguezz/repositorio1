n=int(input("Ingrese cuántas alturas va a ingresar "))
altura=int(input("Ingrese una altura"))
amax=altura
amin=altura
for i in range (1,n+1):
    altura=int(input("Ingrese una altura"))
    if altura>amax:
        amax=altura
    if altura<amin:
        amin=altura
print("La altura más alta es:",amax)
print("La altura más baja es:",amin)
