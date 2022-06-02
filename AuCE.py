import sys


def imprime_resultado(cadena):
    resultado_formato='_'
    for caracter in cadena:
        if caracter=='1':
            resultado_formato=resultado_formato + '*'
        else:
            resultado_formato=resultado_formato + ' '
    print(resultado_formato + "_")

  
def procesa_ventana(ventana):
    caso = int(ventana,2)
    if caso ==0:
        resultado = '1'
    elif caso == 1:
        resultado ='1'
    elif caso == 2:
        resultado ='1'
    elif caso == 3:
        resultado ='1'
    elif caso == 4:
        resultado ='0'
    elif caso ==5:
        resultado ='0'
    elif caso == 6:
        resultado ='0'
    elif caso == 7:
        resultado ='0'
    else:
        resultado ='0'
    
    return resultado

# Generar una nueva cadena de acuerdo a una regla (0-255)
# Entrada: cadena actual (t=i)
# Salida: cadena nueva (t=i+1)
def recorre_cadena(cadena):
    nueva_cadena=''

    for i in range(0,len(cadena)):
        n=len(cadena)
        ventana=cadena[(i+(n-1))%n]+cadena[i]+cadena[(i+1)%n]
        nueva_cadena=nueva_cadena+procesa_ventana(ventana)
            
    return nueva_cadena


#-------------------------------------------------------------
#Main (parte principal del programa)


cadena1="0000000000000000000000000000000000100000000000000000000000000000000000"

cadena_actual=cadena1

iteraciones=sys.argv[1]
print(bin(15))


for i in range(0,int(iteraciones)):
    imprime_resultado(cadena_actual)
    nueva_cadena=recorre_cadena(cadena_actual)
    cadena_actual=nueva_cadena
