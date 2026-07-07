from Validaciones import *
from Funciones import *

lista_legajos = []
lista_apellidos_nombres = []
lista_generos = []
lista_notas_primer_parcial = []
lista_notas_segundo_parcial = []
lista_promedios = []
mayor_promedio = 0 
salir_menu = False 

opcion = 0 
validar_carga = False 
validar_calculo_promedios = False 

while salir_menu == False : 
    print("#----------------------------------------------------------#")
    print("#---- Cargar datos             (1)--)")
    print("#---- Mostrar datos            (2)--)")
    print("#---- Calcular promedio        (3)--)")
    print("#---- Ordenar y mostrar        (4)--)")
    print("#---- Mostrar mayor promedio   (5)--)")
    print("#---- SUBIR DATOS              (9)--)")
    print("#---- Salir                    (10)--)")
    print("#----------------------------------------------------------#")
    opcion = pedir_int_rango("Ingrese opcion ",0 ,13 )
    
    match opcion :
        
        case 1 :
            salir = False 
            legajo_ok = False 
            while salir == False : 
                
                
                aux_carga = pedir_legajo (lista_legajos)      
                lista_legajos = agregar_dato(lista_legajos, aux_carga)
                             
                aux_carga = pedir_str("Ingrese Apellido y nombre : ")         
                lista_apellidos_nombres = agregar_dato(lista_apellidos_nombres, aux_carga)

                aux_carga = pedir_genero ()                
                lista_generos = agregar_dato(lista_generos, aux_carga)                                
                    
                aux_carga = pedir_float_rango("Ingrese nota primer parcial  : ",1,10)                                   
                lista_notas_primer_parcial = agregar_dato(lista_notas_primer_parcial, aux_carga)
                                                                 
                aux_carga = pedir_float_rango("Ingrese nota segundo parcial : ",1,10)                                   
                lista_notas_segundo_parcial = agregar_dato(lista_notas_segundo_parcial, aux_carga)
                
                print("#------ Seguir cargando ( 1 )--) ")
                print("#------ Salir ( 2 )--) ")
                
                opcion = pedir_int_rango("Ingrese opcion ",0 ,2 )
                validar_carga = True
                
                
                if opcion == 2 :
                    break
 
                      
        case 2 :
            if validar_carga == True : 
                
                mostar_alumnos(lista_legajos, 
                    lista_apellidos_nombres, 
                    lista_generos, 
                    lista_notas_primer_parcial, 
                    lista_notas_segundo_parcial)
            else :
                print("#-------- PRIMERO DE CARGAR UN ALUMNO -------#")
                            
            
            
        case 3 :
            if validar_carga == True : 
                lista_promedios = calcular_promedios (lista_notas_primer_parcial,lista_notas_segundo_parcial)
                mayor_promedio = calcular_mayor_promedio(lista_promedios)
                validar_calculo_promedios = True 
                print("#---------- CALCULADO CON EXITO ----------#")
            else :
                print("#-------- PRIMERO DE CARGAR UN ALUMNO -------#")
            
        case 4 :
            if validar_carga == True :
                if validar_calculo_promedios == True :
                    
                    ordenar_por_promedio(lista_promedios,lista_legajos,lista_apellidos_nombres,lista_generos,lista_notas_primer_parcial,lista_notas_segundo_parcial, "DESC" )
                    mostrar_alumnos_con_promedios(lista_legajos, 
                    lista_apellidos_nombres, 
                    lista_generos, 
                    lista_notas_primer_parcial, 
                    lista_notas_segundo_parcial,
                    lista_promedios)
                else : 
                    print ("#-------- PRIMERO DE CALCULAR PROMEDIO --------# ")
            else :
                print("#-------- PRIMERO DE CARGAR UN ALUMNO -------#")
                
        case 5 :
            if validar_carga == True :
                if validar_calculo_promedios == True :
                    mostrar_mayor_promedio ( mayor_promedio,
                                        lista_legajos,
                                        lista_apellidos_nombres,
                                        lista_generos,
                                        lista_notas_primer_parcial,
                                        lista_notas_segundo_parcial,
                                        lista_promedios)
                else : 
                    print ("#-------- PRIMERO DE CALCULAR PROMEDIO --------# ")
            else :
                print("#-------- PRIMERO DE CARGAR UN ALUMNO -------#")
        
        case 6 :
            
            if validar_carga == True :
                if validar_calculo_promedios == True :
                    aux_legajo = pedir_int_rango("Ingrese Legajo : ",0 ,10000 )
                    buscar_y_mostrar(   lista_legajos,
                                        lista_apellidos_nombres,
                                        lista_generos,
                                        lista_notas_primer_parcial,
                                        lista_notas_segundo_parcial,
                                        lista_promedios, 
                                        aux_legajo)
                else : 
                    print ("#-------- PRIMERO DE CALCULAR PROMEDIO --------# ")
            else :
                print("#-------- PRIMERO DE CARGAR UN ALUMNO -------#")
        
        case 7 :
            pass
        
       
        case 9:
            lista_legajos = [1001,1002,1003,1004,1005]
            lista_apellidos_nombres = ["Torres Lucas ","Estevez Santino ","Garrido cecilia","Auad Liliana","Fernandez Micaela"]
            lista_generos = ["x","x","x","x","x"]
            lista_notas_primer_parcial = [2,10,3,5,10]
            lista_notas_segundo_parcial = [9,10,3,1,10]
            validar_carga = True 
            
            print("Datos cargados con exito !! ")
            
        case 10:
            
            print("Cerrando sistema")
            salir_menu = True 