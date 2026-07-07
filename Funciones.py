from Validaciones import *
#-------------------------------------------------------------------------------------------
def pedir_int_rango(mensaje, min , max ):
    
    ''' Funcion que se encarga de pedir un numero al usuario. 
        valida solo numeros y entre un rango solicitado 
    
        Parametros : 
                    Mensaje(str) :  Mensaje de interfaz al usuario
                    min (int) : Indica el rango minimo solicitado 
                    max (int) : Indica el rango maximo solicitado 
        
        Retorno : 
                   retorno (int) Si es correcto RETORNA el valor, caso contrario ERROR
    retorno   : 
    
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

#-------------------------------------------------------------------------------------------

def pedir_genero () :
    '''Funcion que se encarga de solicitar al usuario que ingrese el genero  ( F, M , X ) .
        valida que el genero ingresado se correcto
        si es correcto lo retorna . 
        
        Retorno : 
                    retorno (str) : Si es correcto retorna el genero caso contrario retorna False 

    '''
    retorno = False
    flag = False
    intentos = 0 
    while flag == False :
        aux_sexo = input("Ingrese Genero F/M/X : ")
        validacion_sexo = validar_genero(aux_sexo)
        if validacion_sexo == True  :
                retorno = aux_sexo 
                break 
                       
        else : 
            print("!!!!! __ [ ERROR ] ---  Ingrese una palabra valido (SOLO LETRAS ) __ !!!!! ")
       
    
    return retorno 

#-------------------------------------------------------------------------------------------

def pedir_float_rango(mensaje:str ,num_min:int ,num_max:int ) -> float :
    
    '''Funcion que se encarga de Pedir un numero al usuario.
        Itera con un maximo de 3 intentos pidiendo un numero 
        valida solo numeros y entre un rango solicitado 
        

        Parametros : 
                    Mensaje(str) :  Mensaje de interfaz al usuario
                    min (int) : Indica el rango minimo solicitado 
                    max (int) : Indica el rango maximo solicitado 
        
        Retorno : 
                   retorno (int) : Si es correcto RETORNA el valor, caso contrario ERROR

    '''    
    retorno = False
    flag_salida_while = False
    intentos = 0 
    
    while flag_salida_while == False :
        aux_caracter = input(mensaje)
        aux_flag = validar_flotante(aux_caracter)
         
        if aux_flag == True :
                aux_retorno = float(aux_caracter) 
        
                if aux_retorno >= num_min and aux_retorno <= num_max :
                    retorno = float(aux_caracter) 
                    break        
        else : 
            print("!!!!! __  [ ERROR ] ---  Ingrese un nunero valido __ !!!!! 3/ ")

    return retorno

#-------------------------------------------------------------------------------------------

def pedir_str(mensaje):
    '''Funcion que se encarga de pedir un strg o char al usuario 
        Itera con un maximo de 3 intentos 
        Valida solo letras 
    
        Parametro : 
                    Mensaje(str): Mensaje de interfaz al usuario
        Retorno :
                retorno (str) Si es correcto retorna el str, caso contrario False 
        retorno   : 
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

#-------------------------------------------------------------------------------------------

def mostrar_alumno(legajo:int, 
                   apellidos_nombres : str, 
                   genero:str, 
                   nota_1:float, 
                   nota_2:float) :

    '''Funcion que se encarga de Recibir los datos de un alumno y lo muestra de forma ordenado 

        Paramentros :
                    legajo (int) : contiene el numero de legajo del alumno 
                    apellidos_nombres (str) : contiene el apellido y nombre del alumno
                    genero (str) :  contiene el genero del alumno 
                    nota_1 (float) : contiene la nota del primer parcial de alumno 
                    nota_2 (float) : contiene la nota del segundo parcial de la alumno 
                    
     
    '''
    print(f"{legajo:<10}{" | "}{apellidos_nombres:<25}{ " | " }{genero:<10}{" | "}{nota_1:<10}{" | "}{nota_2:<10}")

#-------------------------------------------------------------------------------------------

def mostar_alumnos(lista_legajos:list, 
                   lista_apellidos_nombres : list, 
                   lista_generos:list, 
                   lista_notas_1:list, 
                   lista_notas_2:list,
                   ) :
    ''' Funcion que se encarga de recorrer la lista de legajos asociados a cada alumno y mostrarlos.
        Cada vez que recorre llama a la funcion encargada de mostar un alumno y le pasa el alumno

        Parametros :        
                    lista_legajos (list) , contiene una lista de legajos del alumno
                    lista_apellidos_nombres (list) , contiene una lista con appelidos y nombres del alumno 
                    lista_generos  (list) , contiene una lista de generos de cada alumno
                    lista_notas_1  (list) , contiene una lista de notas del primer parcial 
                    lista_notas_2  (list) , contiene una lista de notas del segundo parcial 
    '''
    titulos()
    for i in range(len(lista_legajos)) :
        mostrar_alumno(lista_legajos[i], 
                   lista_apellidos_nombres [i], 
                   lista_generos[i], 
                   lista_notas_1[i], 
                   lista_notas_2[i],
                   )

#-------------------------------------------------------------------------------------------

def mostrar_alumno_con_promedio(legajo:int, 
                   apellidos_nombres : str, 
                   genero:str, 
                   nota_1:float, 
                   nota_2:float,
                   promedio:float) :
                       
  
    '''Funcion que se encarga de Recibir los datos de un alumno y lo muestra de forma ordenado 

        Paramentros :
                    legajo (int) : contiene el numero de legajo del alumno 
                    apellidos_nombres (str) : contiene el apellido y nombre del alumno
                    genero (str) :  contiene el genero del alumno 
                    nota_1 (float) : contiene la nota del primer parcial de alumno 
                    nota_2 (float) : contiene la nota del segundo parcial de la alumno 
                    promedio (float) : contiene el promedio del alumno 
     
    ''' 
    print(f"{legajo:<10}{" | "}{apellidos_nombres:<25}{" | "}{genero:<10}{" | "}{nota_1:<10}{" | "}{nota_2:<10}{" | "}{promedio:<10}")



def mostrar_alumnos_con_promedios(lista_legajos:list, 
                   lista_apellidos_nombres : list, 
                   lista_generos:list, 
                   lista_notas_1:list, 
                   lista_notas_2:list,
                   lista_promedios : list ) :
                       
    '''Funcion que se encarga de recorrer la lista de legajos asociados a cada alumno y mostrarlos.
        Cada vez que recorre llama a la funcion encargada de mostar un alumno y le pasa el alumno

        Parametros :        
                    lista_legajos (list) , contiene una lista de legajos del alumno
                    lista_apellidos_nombres (list) , contiene una lista con appelidos y nombres del alumno 
                    lista_generos  (list) , contiene una lista de generos de cada alumno
                    lista_notas_1  (list) , contiene una lista de notas del primer parcial 
                    lista_notas_2  (list) , contiene una lista de notas del segundo parcial
                    lista_promedios (list) , contiene una lista de promedios 

    '''
    titulos_con_promedios()
    for i in range(len(lista_legajos)) :
        mostrar_alumno_con_promedio(lista_legajos[i], 
                   lista_apellidos_nombres [i], 
                   lista_generos[i], 
                   lista_notas_1[i], 
                   lista_notas_2[i],
                   lista_promedios[i]
                   )

#-------------------------------------------------------------------------------------------
        
def agregar_dato(lista : list, dato : any ) -> list :
    
    '''Funcion que se encarga de agregar un dato dentro de la lista 
        
        Parametros:
                    lista (list) : Lista a modificar 
                    dato (any) : dato a almacenar en lista 
                    
        Retornos : 
                    lista (list) : Devuelve la lista con el dato agregado 
    '''

    lista = lista + [dato]

    return lista

#-------------------------------------------------------------------------------------------

def sumar (numero_1 : float  , numero_2 : float  ) -> float : 
    '''Funcion que se encarga de sumar dos variables 
        
        parametro : 
                    numero_1 (float) : Primer número 
                    numero_1 (float) : Segundo número 
                    
        Retorno : 
                    total (float) : Retorna el total de la suma de ambos numeros 
    
    '''
    
    total = numero_1 + numero_2
    
    return total 
    
def calcular_promedios (lista_notas_1,lista_notas_2) :
    
    '''Funcion que se encarga de calcular un promedio de dos notas.
        Suma ambas notas y luego las divide por 2 para sacar el promedio 
        
        Parametros : 
                    lista_notas_1 (list) : Primer nota a sumar
                    lista_notas_2 (list) : Segunda nota a sumar 
                    
        Retornos : 
                    aux_lista_promedios (list) : Retorna una nueva lista que contiene los promedios de cada alumno 
    '''
    
    aux_lista_promedios = []
    
    for i in range(len(lista_notas_1)):
        aux_suma = sumar(lista_notas_1[i],lista_notas_2[i])
        aux_total = aux_suma / 2
        aux_lista_promedios = agregar_dato(aux_lista_promedios, aux_total)
    
    return aux_lista_promedios

#-------------------------------------------------------------------------------------------

def calcular_mayor_promedio(lista_promedios : list ) : 
    
    '''Funcion que se encarga de  recorrer una lista de promedios , buscar el mayor y retornarlo
        
        Parametro : 
                    lista_promedios (list) : Lista de promedios de alumnos 
                    
        Retornos :
                    aux_mayor(float) : Retorna el mayor promedio econtrado 
    '''
    
    aux_mayor = 0 
    
    for promedio in lista_promedios : 
        if aux_mayor < promedio :
            aux_mayor = promedio 
            
    return aux_mayor

#-------------------------------------------------------------------------------------------

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
    
#-------------------------------------------------------------------------------------------    
    
def ordenar_por_promedio(lista_promedios,
                         lista_legajos,
                         lista_apellidos_nombres,
                         lista_generos,
                         lista_notas_primer_parcial,
                         lista_notas_segundo_parcial,
                         criterio : str = "ASC" ):

    
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
 
#-------------------------------------------------------------------------------------------

def ordenar_lista(lista:list, criterio:str = "ASC") -> list:
    
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista) ):  
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]): 
                
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista

#-------------------------------------------------------------------------------------------

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
    
#-------------------------------------------------------------------------------------------
    
def validar_legajo (lista_legajos : list , legajo_a_buscar : int) : 

    for legajo in lista_legajos : 
        if legajo == legajo_a_buscar : 
            return True
    
    return False
            
#-------------------------------------------------------------------------------------------

def buscar_y_mostrar(   lista_legajos : list,
                        lista_apellidos_nombres : list,
                        lista_generos : list,
                        lista_notas_primer_parcial : list,
                        lista_notas_segundo_parcial : list,
                        lista_promedios : list, 
                        item : int ) :

    '''
        Recibe un dato , recorre  y lo busca dentro de la lista 
        si lo encuentra muestra todos los datos del alumno

        parametro : lista_legajos : list , contiene una lista de legajos del alumno
        parametro : lista_apellidos_nombres : list , contiene una lista con appelidos y nombres del alumno 
        parametro : lista_generos : list , contiene una lista de generos de cada alumno
        parametro : lista_notas_1 : list , contiene una lista de notas del primer parcial 
        parametro : lista_notas_2 : list , contiene una lista de notas del segundo parcial 
        parametro : lista_promedios : list , contiene una lista de promedios
        parametro : item : int , contiene el dato a buscar 
        
    '''
    for i in range(len(lista_legajos)):
         if lista_legajos[i] == item :
            mostrar_alumno_con_promedio(lista_legajos[i], 
                   lista_apellidos_nombres[i], 
                   lista_generos[i], 
                   lista_notas_primer_parcial[i], 
                   lista_notas_segundo_parcial[i],
                   lista_promedios[i])
            
            
def titulos_con_promedios() :
    
    print(f"{'Legajo ':<10}{" | "}{' Apellidos y nombres':<25}{" | "}{' Genero':<10}{" | "}{' Nota_1':<10}{" | "}{' Nota_2':<10}{' Promedio':<10}")
    print("#----------------------------------------------------------------------------------------#")
    
def titulos () :
    
    print(f"{'Legajo ':<10}{" | "}{' Apellidos y nombres':<25}{" | "}{' Genero':<10}{" | "}{' Nota_1':<10}{" | "}{' Nota_2':<10}")
    print("#----------------------------------------------------------------------------------------#")
#-------------------------------------------------------------------------------------------