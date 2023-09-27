print("Ingrese el primer coeficiente")
a=int(input())
print("Ingrese el segundo coficiente")
b=int(input())
print("Ingrese el tercer coeficiente")
c=int(input())

x1=(-b+((b*b)-4*a*c)**0.5)/2*a
x2=(-b-((b*b)-4*a*c)**0.5)/2*a
print("La respuesta es",x1," y " ,x2)
