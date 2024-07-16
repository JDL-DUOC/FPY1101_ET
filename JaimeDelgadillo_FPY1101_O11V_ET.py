import os
import time
import csv
import random

trabajadores=["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel,Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
diccitrabajadores={}
sueldosmenor8={}
sueldosentre8y2={}
sueldosmayor2={}
listafinal=[]

def asignar_sueldos():
    os.system("cls")
    for lista in trabajadores:
        sueldoaliatorio=random.randint (300000,2500000)
        diccitrabajadores[lista]=sueldoaliatorio
    
    for nom,sue in diccitrabajadores.items():
        if sue < 800000:
            sueldosmenor8[nom]=sue
        elif sue <2000000 and sue >=800000:
            sueldosentre8y2[nom]=sue
        elif sue > 2000000 :
            sueldosmayor2[nom]=sue    
    print ("\nNuevo Dicionario con sueldos aleatorios")
    print (diccitrabajadores)
    print ("\nListado de trabajadores con sueldo menor que $800.000")    
    print (sueldosmenor8)
    print ("\nListado de trabajadores con sueldos entre $ 800.000 y $ 2.000.000")
    print (sueldosentre8y2)
    print ("\nLista de trabajadores con sueldos mayores a $ 2.000.000")
    print (sueldosmayor2)
    tecla=input("Presione [ENTER] para continuar ...")
    #print(diccitrabajadores)

def clasificar_sueldos():
    os.system("cls")
    tammenor8=len(sueldosmenor8)
    tamentre8y2=len(sueldosentre8y2)
    tammayor2=len(sueldosmayor2)    
    
    print (f"\nSueldos menores a $ 800.000 : {tammenor8}")
    print ("Nombre Empleado\t\tSueldo")
    for i,c in sueldosmenor8.items():
        print (f"{i}\t\t    {c}")

    print (f"\nSueldo entre $ 800.000 y $ 2.000.000 : {tamentre8y2}")
    print ("Nombre Empleado\t\tSueldo")
    for i1,c1 in sueldosentre8y2.items():
        print (f"{i1}\t\t  {c1}") 

    print (f"\nSueldo superiores a $2.000.000 :{tammayor2} ")
    print ("Nombre Empleado\t\tSueldo")
    for i2,c2 in sueldosmayor2.items():
        print (f"{i2}\t\t   {c2}")
      
    tecla=input("Presione [ENTER] para continuar ...")

def estadisticas():
    os.system("cls")
    dic=len(diccitrabajadores.items())
    sueldomasalto=max(diccitrabajadores.values())
    sueldomasbajo=min(diccitrabajadores.values())
    sumasueldos = sum(diccitrabajadores.values())
    promediosueldos =sumasueldos / len(diccitrabajadores.items())
    producto=1
    for r in diccitrabajadores.values():
        producto *= r
    media=producto**(1/dic)
    print (f"El suedo mas alto es           : {sueldomasalto} ")
    print (f"El sueldo mas bajo es          : {sueldomasbajo} ")
    print (f"El promedio de los sueldos son : {promediosueldos}")
    print (f"La media geometrica es         : {media}")

    tecla=input("Presione [ENTER] para continuar ...")

def reportes_sueldos():
    os.system("cls")
    for x,y in diccitrabajadores.items():
        listafinal.append([x,y,(y*0.07),(y*0.12),(y-(y*0.07)-(y*0.12))])    
    cabecera=(["Nombre Empleado","Sueldo base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
    print (cabecera)
    for f in listafinal:
        print(f)
    
    with open ("Datos_Sueldos.csv","w", newline="") as archi:
        escritor=csv.writer(archi)
        escritor.writerow(cabecera)
        escritor.writerows(listafinal)
    
    print ("\nEl archivo [Datos_Sueldos.csv] se he creado exitosamente.")
    tecla=input("Presione [ENTER] para continuar ...")
    

def menu():
    
    princi=True
    while princi==True:
        os.system ("cls")
        print ("[1]..Asignar Sueldos aleatorios\n[2]..Clasificar sueldos\n[3]..Ver estadisticas\n[4]..Reportes de sueldos\n[5]..Salir de programa")
        try:
            opc=int(input("Elija Opcion :"))
        except ValueError:
            print ("Error, debe ser un valor numerico ")
            time.sleep(2)
            continue
        if opc==1:
            asignar_sueldos()
        elif opc==2:
            clasificar_sueldos()
        elif opc==3:
            estadisticas()
        elif opc==4:
            reportes_sueldos()
        elif opc==5:
            os.system("cls")
            print("Finalizando Programa..\nDesarrollado por Jaime Delgadillo L.\nRUT 13.288.842-6")
            break
        else:
            print ("Error, el digito ingresado no esta en el menu")
            time.sleep(2)
            continue


menu()


    