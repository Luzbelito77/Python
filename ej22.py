print("Ingrese Edad")
e=int(input())
print("Ingrese Ingresos")
i=int(input())
if e > 15:
    if i>500:
        print("DEBE PAGAR IMPUESTOS")
    else:
        print("No debe pagar impustos")
else:
    print("No debe pagar impustos")