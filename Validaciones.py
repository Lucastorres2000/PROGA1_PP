'''
    Valida que una cadena de caracteres sea un numero flotante 
    
    parametro : caracteres . variable de tipo str , almacena cadena a analizar
    retorna   : Si es solo numeros True , caso contrario False 

'''


def validar_flotante(cadena : str ):
    retorno = True
    cantidad_puntos = 0

    for c in cadena:
        
        if ord(c) >= 48 and ord(c) <= 57:
            pass

        elif c == ".":
            cantidad_puntos += 1

            if cantidad_puntos > 1:
                retorno = False
                return retorno 

        
        else:
            retorno = False

    return retorno

'''
    Valida que una cadena de caracteres sea solo numeros
    
    parametro : caracteres . variable de tipo str , almacena cadena a analizar
    retorna   : Si es solo numeros True , caso contrario False 

'''
def validar_int(caracteres : str ):
    for c in caracteres:
        if c < '0' or c > '9':
            return False
    return True


'''
    Valida que un numero sea par 
    
    parametros : numero , variable de tipo int que contiene el numero a analizar 
    
    return : True si es par , False si es impar 
'''

def validar_par(numero: int) -> bool:
    
    retorno = False 
    
    if numero % 2 == 0 :
        retorno = True
        
    return retorno 
#---------------------------------------------------------------------------------------------------------------------------------

'''
    Valida que los caracteres sean solo letras 
    
    parametros : caracteres, contiene los caracteres a analizar 
    
    return  : True si es solo letras, False si hay otros caracteres 
'''

def validar_char(caracteres:str):
    retorno = True
    for c in caracteres:
        c_aux = ord(c)
        if not ((65 <= c_aux <= 90) or (97 <= c_aux <= 122)):
            retorno = False
    return retorno    
#--------------------------------------------------------------------------------------------------

def convertir_a_mayuscula(caracteres:str):
    retorno = caracteres
    if ord(caracteres) >= 97 and ord(caracteres) <= 122:
        valor = ord(caracteres) - 32
        retorno = chr(valor)
    
    return retorno
    
 
 #---------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------
def convertir_a_minuscula (caracteres:str):
    retorno = caracteres
    if ord(caracteres) >= 65 and ord(caracteres) <= 90:
        valor = ord(caracteres) + 32
        retorno = chr(valor)
        
    return retorno
#------------------------------------------------------------------------------------------------------------------
'''
    Valida que los caracteres sean F - M - X 
    
    parametros : caracteres , variable de tipo str, contiene el caracter a analizar
    
    return : True si es F-M-X / caso contrario False 
'''

def validar_genero(caracteres:str):
    retorno = True
    caracteres = convertir_a_mayuscula(caracteres)
    if caracteres != 'F' and caracteres != 'M' and caracteres != 'X':
        retorno = False
    
    return retorno
#---------------------------------------------------------------------------------------------------------------------------------
