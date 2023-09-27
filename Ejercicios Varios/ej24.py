print("Ingrese la masa del individuo en libras")
p1=int(input())
print("Ingrese la altura del individuo en cm")
a1=int(input())
p=p1*0.453592
a=a1/100
imc=p/(a*a)
if imc<=16:
    print("El peso es : ",p,"Criterio de ingreso, ",imc)
elif imc>16 and imc<16.9:
    print("El peso es : ",p,",Infrapeso, ",imc)
elif imc>17 and imc<18.4:
    print("El peso es : ",p,",Bajo Peso, ",imc)
elif imc>18.5 and imc<4.9:
    print("El peso es : ",p,",Peso Normal, ",imc)
elif imc>25 and imc<29.9:
    print("El peso es : ",p,",Sobrepeso, ",imc)
elif imc>30 and imc<34.9:
    print("El peso es : ",p,",Obesidad Premorbida, ",imc)
elif imc>40 and imc<45:
    print("El peso es : ",p,",Obesidad morbida, ",imc)
