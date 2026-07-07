from Validaciones import *

def pedir_int_rango(mensaje, min , max ):
    
    '''
        Pide un numero al usuario.
        Itera con un maximo de 3 intentos pidiendo un numero 
        valida solo numeros y entre un rango solicitado 
    

    parametro : Mensaje , Mensaje de interfaz al usuario
    parametro : min , Indica el rango minimo solicitado 
    parametro : max , Indica el rango maximo solicitado 
    retorno   : Si es correcto RETORNA el valor, caso contrario ERROR
    
    '''

    retorno = False
    flag_salida_while = False
    
    
    while flag_salida_while == False  :
        aux_caracter = input(mensaje)
        aux_flag = validar_int(aux_caracter )
        
        if aux_flag == True :
                aux_retorno = int(aux_caracter) 
                
                if aux_retorno >= min and aux_retorno <= max :
                    retorno = int(aux_caracter) 
                    return retorno 
                
                else : 
                    print("!!!!! __  [ ERROR ] ---  Ingrese una opcion valida __ !!!!!  ")
                
        else : 
            print("!!!!! __  [ ERROR ] ---  Ingrese un numero valido __ !!!!!  ")
         
    return retorno

def pedir_genero () :
    retorno = False
    flag = False
    intentos = 0 
    while flag == False and intentos  < 3 :
        aux_sexo = input("Ingrese Genero F/M/X : ")
        validacion_sexo = validar_genero(aux_sexo)
        if validacion_sexo == True  :
                retorno = aux_sexo 
                break 
                       
        else : 
            print("!!!!! __ [ ERROR ] ---  Ingrese una palabra valido (SOLO LETRAS ) __ !!!!! ")
        intentos = intentos + 1 
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
    
    return retorno 


 
def pedir_float_rango(mensaje:str ,num_min:int ,num_max:int ) -> float :
    
    '''
        Pide un numero al usuario.
        Itera con un maximo de 3 intentos pidiendo un numero 
        valida solo numeros y entre un rango solicitado 
        Si es correcto RETORNA el valor, caso contrario ERROR

        parametro : Mensaje , Mensaje de interfaz al usuario
        parametro : min , Indica el rango minimo solicitado 
        parametro : max , Indica el rango maximo solicitado 

    '''
    
    retorno = False
    flag_salida_while = False
    intentos = 0 
    
    while flag_salida_while == False and intentos  <= 3 :
        aux_caracter = input(mensaje)
        aux_flag = validar_flotante(aux_caracter)
        intentos = intentos + 1 
        if aux_flag == True :
                aux_retorno = float(aux_caracter) 
                
                if aux_retorno >= num_min and aux_retorno <= num_max :
                    retorno = float(aux_caracter) 
                    break
                
                
        else : 
            print("!!!!! __  [ ERROR ] ---  Ingrese un nunero valido __ !!!!! 3/ ")
        
        
        if intentos == 4 :
            print("!!!!! __ [ ERROR ] ---  Limite de intentos __ !!!!! ")
    return retorno

def pedir_str(mensaje):
    '''
        Pide un strg o char al usuario 
        Itera con un maximo de 3 intentos 
        Valida solo letras 
    
        parametro : Mensaje , Mensaje de interfaz al usuario
        retorno   : Si es correcto retorna el str, caso contrario ERROR
    '''
    
    retorno = False
    flag = False
    while flag == False :
        aux_caracter = input(mensaje)
        flag = validar_char(aux_caracter)
        
        if flag == True :
                return aux_caracter 
                
                
        else : 
            print("!!!!! __ [ ERROR ] ---  Ingrese una palabra valida (SOLO LETRAS ) __ !!!!! ")
        

            
    return retorno

def mostrar_alumno(legajo:int, 
                   apellidos_nombres : str, 
                   genero:str, 
                   nota_1:float, 
                   nota_2:float) :
    print(f"{legajo:<10}{apellidos_nombres:<25}{genero:<10}{nota_1:<10}{nota_2:<10}")



def mostar_alumnos(lista_legajos:list, 
                   lista_apellidos_nombres : list, 
                   lista_generos:list, 
                   lista_notas_1:list, 
                   lista_notas_2:list,
                   ) :
    
    for i in range(len(lista_legajos)) :
        mostrar_alumno(lista_legajos[i], 
                   lista_apellidos_nombres [i], 
                   lista_generos[i], 
                   lista_notas_1[i], 
                   lista_notas_2[i],
                   )
        
def mostrar_alumno_con_promedio(legajo:int, 
                   apellidos_nombres : str, 
                   genero:str, 
                   nota_1:float, 
                   nota_2:float,
                   promedio:float) :
    print(f"{legajo:<10}{apellidos_nombres:<25}{genero:<10}{nota_1:<10}{nota_2:<10}{promedio:<10}")



def mostrar_alumnos_con_promedios(lista_legajos:list, 
                   lista_apellidos_nombres : list, 
                   lista_generos:list, 
                   lista_notas_1:list, 
                   lista_notas_2:list,
                   lista_promedios : list ) :
    
    for i in range(len(lista_legajos)) :
        mostrar_alumno_con_promedio(lista_legajos[i], 
                   lista_apellidos_nombres [i], 
                   lista_generos[i], 
                   lista_notas_1[i], 
                   lista_notas_2[i],
                   lista_promedios[i]
                   )
        
        
def agregar_dato(lista:list, dato:str):

    lista = lista + [dato]

    return lista

def calcular_promedios (lista_notas_1,lista_notas_2) :
    
    aux_lista_promedios = []
    
    for i in range(len(lista_notas_1)):
        aux_suma = lista_notas_1[i] + lista_notas_2[i]
        aux_total = aux_suma / 2
        aux_lista_promedios = agregar_dato(aux_lista_promedios, aux_total)
    
    return aux_lista_promedios

def calcular_mayor_promedio(lista_promedios : list ) : 
    
    aux_mayor = 0 
    
    for promedio in lista_promedios : 
        if aux_mayor < promedio :
            aux_mayor = promedio 
            
    return aux_mayor


def mostrar_mayor_promedio ( promedio_max : int,
                        lista_legajos : list,
                        lista_apellidos_nombres : list,
                        lista_generos : list,
                        lista_notas_primer_parcial : list,
                        lista_notas_segundo_parcial : list,
                        lista_promedios : list) :
    
    for i in range(len(lista_promedios)): 
        if lista_promedios[i]  == promedio_max :
            mostrar_alumno_con_promedio( lista_legajos[i], 
                            lista_apellidos_nombres[i], 
                            lista_generos[i], 
                            lista_notas_primer_parcial[i], 
                            lista_notas_segundo_parcial[i],
                            lista_promedios[i]) 
    
    
    
def ordenar_por_promedio(lista_promedios,lista_legajos,lista_apellidos_nombres,lista_generos,lista_notas_primer_parcial,lista_notas_segundo_parcial,criterio : str = "ASC" ):

    
    for i in range(len(lista_promedios) - 1):
        for j in range(i + 1, len(lista_promedios)):
            if (criterio == "ASC" and lista_promedios[i] > lista_promedios[j]) or (criterio == "DESC" and lista_promedios[i] < lista_promedios[j]): 
                
                aux = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = aux 
                
                aux = lista_legajos[i]
                lista_legajos[i] = lista_legajos[j]
                lista_legajos[j] = aux
                
                aux = lista_apellidos_nombres[i]
                lista_apellidos_nombres[i] = lista_apellidos_nombres[j]
                lista_apellidos_nombres[j] = aux
                
                aux = lista_generos[i]
                lista_generos[i] = lista_generos[j]
                lista_generos[j] = aux
                
                aux = lista_notas_primer_parcial[i]
                lista_notas_primer_parcial[i] = lista_notas_primer_parcial[j]
                lista_notas_primer_parcial[j] = aux
                
                aux = lista_notas_segundo_parcial[i]
                lista_notas_segundo_parcial[i] = lista_notas_segundo_parcial[j]
                lista_notas_segundo_parcial[j] = aux           
 



def ordenar_lista(lista:list, criterio:str = "ASC") -> list:
    
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista) ):  
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]): 
                
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista


def pedir_legajo (lista_legajos : list ) : 
    
    legajo_valido = False
    
    retorno = False 
    while legajo_valido == False : 
        aux_carga = pedir_int_rango("Ingrese legajo ",0 ,10000 )
        aux = validar_legajo (lista_legajos,aux_carga)
        
        if aux == False : 
            retorno = aux_carga
            legajo_valido = True 
            
        else : 
            print("#-------- ESTE LEGAJO YA EXISTE --------#")
     
    return retorno 
    
    
    
    
    
def validar_legajo (lista_legajos : list , legajo_a_buscar : int) : 
    
    for legajo in lista_legajos : 
        if legajo == legajo_a_buscar : 
            return True
    
    return False
            
            
def buscar_y_mostrar(   lista_legajos : list,
                        lista_apellidos_nombres : list,
                        lista_generos : list,
                        lista_notas_primer_parcial : list,
                        lista_notas_segundo_parcial : list,
                        lista_promedios : list, 
                        item : int ) :
    
    for i in range(len(lista_legajos)):
         if lista_legajos[i] == item :
            mostrar_alumno_con_promedio(lista_legajos[i], 
                   lista_apellidos_nombres[i], 
                   lista_generos[i], 
                   lista_notas_primer_parcial[i], 
                   lista_notas_segundo_parcial[i],
                   lista_promedios[i])
            
    
   
    
            

                 
            
                        