#codigo para manejar las cuentas y ver gastos etc
#Jose Ignacio Paez
import csv
import time
pichinchaGASTOS=[]
santanderGASTOS=[]
efectivoGASTOS=[]

pichinchaG=[]
santanderG=[]
efectivoG=[]


archivo = open('GASTOS.csv', 'r')
reader = csv.reader(archivo)
for i, row in enumerate(reader):
    if i==0:
        pichinchaG = row[0]
        pichinchaGASTOS.append(float(pichinchaG))
    elif i==1:
        santanderG = row[0]
        santanderGASTOS.append(float(santanderG))
    elif i==2:
        efectivoG = row[0]
        efectivoGASTOS.append(float(efectivoG))
archivo.close()

def update_bankP(pichinchaGASTOS):
    archivo = open("GASTOS.csv", "r")  # open file for reading
    rows = csv.reader(archivo)
    data = list(rows)  # convert rows to list
    archivo.close()  # close file
    data[0][0] = pichinchaGASTOS  # update value in second row
    archivo = open("GASTOS.csv", "w", newline="")
    writer = csv.writer(archivo)
    writer.writerows(data)  # write updated data to file
    archivo.close()  # close file
    
def update_bankS(santanderGASTOS):
    # read the csv file
    archivo = open("GASTOS.csv", "r")
    reader = csv.reader(archivo)
    data = list(reader)
    # update value in second row
    data[1][0] = santanderGASTOS
    # write updated data back to csv file
    archivo = open("GASTOS.csv", "w", newline="")
    writer = csv.writer(archivo)
    writer.writerows(data)
    archivo.close()

def update_bankE(efectivoGASTOS):
    archivo = open("GASTOS.csv", "r")  # open file for reading
    rows = csv.reader(archivo)
    data = list(rows)  # convert rows to list
    archivo.close()  # close file
    data[2][0] = efectivoGASTOS  # update value in second row
    archivo = open("GASTOS.csv", "w", newline="")
    writer = csv.writer(archivo)
    writer.writerows(data)  # write updated data to file
    archivo.close()  # close file
    
    



def Pichi(pichinchaGASTOS):
    p=pichinchaGASTOS[0]
    pichincha=[]
    pichincha.append(p)
    print("\nBanco Pichincha") 
    pichincha=[round(pichincha, 2) for pichincha in pichincha]
    print (f"{pichincha} $")
    
    
def Sant(santanderGASTOS):
    s=santanderGASTOS[0]
    santander=[]
    santander.append(s)
    print("\n\nBanco Santander") 
    print (f"{santander} MXN$")
    
def Cash(efectivoGASTOS):
    e=efectivoGASTOS[0]
    efectivo=[]
    efectivo.append(e)
    print("\n\nEFECTIVO") 
    print (f"{efectivo} MXN$")

z=True


while z:
    print("\n\nMENU")
    print("""\t\tSelecciona una opcion
    
    1. VER TUS CUENTAS
    
    2. PONER O RESTAR GASTOS
    
    3. SALIR
    """)
    
    n=int(input())
    if n==1:
        while n==1:
            bancopichincha=Pichi(pichinchaGASTOS)
            time.sleep(3)
            bancosantander=Sant(santanderGASTOS)
            time.sleep(3)
            efectivo=Cash(efectivoGASTOS)
            time.sleep(3)
            m=int(input("\n\n\n\nDeseas salir al menu: \n\n1.MENU \n\n2.Salir\n\n"))
            if m==1:
                break
            else:
                print("\n\nSALIENDO...")
                time.sleep(1)
                z=False
                n=n-1
                
    if n==2:
        while n!=5:
            n=int(input("\n\n\t\tQue cuenta deseas vizualizar, \n\n1.Pichincha \n\n2.Santander \n\n3.Efectivo \n\n4.Inventario de gastos o ingresos \n\n5.SALIR\n\n"))
            if n==1:
                #pichinchaGASTOS=[1]
                time.sleep(2)
                pichinchaGASTOS=[round(pichinchaGASTOS, 2) for pichinchaGASTOS in pichinchaGASTOS]
                print(f"El actual valor de pichincha es:{pichinchaGASTOS} $")
                time.sleep(3)
                r=int(input("\n\n\t\tElige una operacion: \n\n1.Anadir \n\n2.Restar \n\n3.Salir\n\n"))
                if r==1:
                    while True:
                        cant=0
                        cant=float(input("Cantidad a anadir: "))
                        pichi=pichinchaGASTOS[0]
                        cant=cant+pichi
                        pichinchaGASTOS[0]=cant
                        time.sleep(2)
                        actualizar_valor=update_bankP(pichinchaGASTOS[0])
                        pichinchaGASTOS=[round(pichinchaGASTOS, 2) for pichinchaGASTOS in pichinchaGASTOS]
                        print(f"Nuevo valor de cuenta =", pichinchaGASTOS,"USD$")
                        time.sleep(2)
                        break
                    pichinchaGASTOS[0]=pichinchaGASTOS[0]
                if r==2:
                     while True:
                        cant=0
                        cant=float(input("Cantidad a restar: "))
                        pichi=pichinchaGASTOS[0]
                        cant=pichi-cant
                        pichinchaGASTOS[0]=cant
                        time.sleep(2)
                        actualizar_valor=update_bankP(pichinchaGASTOS[0])
                        pichinchaGASTOS=[round(pichinchaGASTOS, 2) for pichinchaGASTOS in pichinchaGASTOS]
                        print(f"Nuevo valor de cuenta =" ,pichinchaGASTOS,"USD$")
                        time.sleep(2)
                        break
                if r==3:
                    print("SALIENDO...")
                    time.sleep(1)
                    break
            if n==2:
                #santanderGASTOS=[1]
                santanderGASTOS=[round(santanderGASTOS, 2) for santanderGASTOS in santanderGASTOS]
                print("\n\nEl actual valor de Santander es:",santanderGASTOS,"MXN \n\n")
                time.sleep(3)
                r=int(input("\n\nElige una operacion: \n\n1.Anadir \n\n2.Restar \n\n3.Salir\n\n"))
                if r==1:
                    while True:
                        cant=0
                        cant=float(input("\n\nCantidad a anadir: \n\n"))
                        sant=santanderGASTOS[0]
                        cant=sant+cant
                        santanderGASTOS[0]=cant
                        time.sleep(2)
                        actualizar_valor=update_bankS(santanderGASTOS[0])
                        santanderGASTOS=[round(santanderGASTOS, 2) for santanderGASTOS in santanderGASTOS]
                        print(f"\n\nNuevo valor de cuenta =", santanderGASTOS,"MXN\n\n")
                        time.sleep(2)
                        break
                if r==2:
                     while True:
                        cant=0
                        cant=float(input("\n\nCantidad a restar: \n\n"))
                        sant=santanderGASTOS[0]
                        cant=sant-cant
                        santanderGASTOS[0]=cant
                        time.sleep(2)
                        actualizar_valor=update_bankS(santanderGASTOS[0])
                        santanderGASTOS=[round(santanderGASTOS, 2) for santanderGASTOS in santanderGASTOS]
                        print(f"\n\nNuevo valor de cuenta =", santanderGASTOS,"MXN\n\n")
                        time.sleep(2)
                        break
                if r==3:
                    print("\n\nSALIENDO...")
                    time.sleep(1)
                    break
            if n==3:
                #efectivoGASTOS=[1]
                efectivoGASTOS=[round(efectivoGASTOS, 2) for efectivoGASTOS in efectivoGASTOS]
                print(f"\n\nEl efectivo que se tiene es:",efectivoGASTOS ,"$MXN\n\n")
                time.sleep(3)
                r=int(input("\n\nElige una operacion: \n\n1.Anadir \n\n2.Restar \n\n3.Salir\n\n"))
                if r==1:
                    while True:
                        cant=0
                        cant=float(input("\nCantidad a anadir: \n"))
                        time.sleep(1)
                        currency=int(input("\n\n1. PESOS MEXICANOS \n\n2.DOLARES AMERICANOS\n\n"))
                        if currency==1:
                            cash=efectivoGASTOS[0]
                            cant=cash+cant
                            efectivoGASTOS[0]=cant
                            time.sleep(2)
                            actualizar_valor=update_bankE(efectivoGASTOS[0])
                            efectivoGASTOS=[round(efectivoGASTOS, 2) for efectivoGASTOS in efectivoGASTOS]
                            print(f"\n\nNuevo valor de cuenta =" ,efectivoGASTOS,"MXN\n\n")
                            time.sleep(1)
                            break
                                   
                        elif currency==2:
                            time.sleep(2)
                            print("TODOS LOS GASTOS O INGRESOS DE EFECTIVO SERAN DICTADOS EN PESOS (18.20 CONVERSION)")
                            time.sleep(2)
                            cant=cant*18.20
                            cash=efectivoGASTOS[0]
                            cant=cash+cant
                            efectivoGASTOS[0]=cant
                            time.sleep(2)
                            actualizar_valor=update_bankE(efectivoGASTOS[0])
                            efectivoGASTOS=[round(efectivoGASTOS, 2) for efectivoGASTOS in efectivoGASTOS]
                            print(f"\n\nNuevo valor de cuenta =" ,efectivoGASTOS,"MXN\n\n")
                            time.sleep(1)
                            break
                if r==2:
                     while True:
                        cant=0
                        cant=float(input("\nCantidad a restar: \n"))
                        time.sleep(1)
                        currency=int(input("\n\n1. PESOS MEXICANOS \n\n2.DOLARES AMERICANOS\n\n"))
                        if currency==1:
                            cash=efectivoGASTOS[0]
                            cant=cash-cant
                            efectivoGASTOS[0]=cant
                            time.sleep(2)
                            actualizar_valor=update_bankE(efectivoGASTOS[0])
                            efectivoGASTOS=[round(efectivoGASTOS, 2) for efectivoGASTOS in efectivoGASTOS]
                            print(f"\n\nNuevo valor de cuenta =" ,efectivoGASTOS,"MXN\n\n")
                            time.sleep(1)
                            break
                                   
                        elif currency==2:
                            time.sleep(2)
                            print("TODOS LOS GASTOS O INGRESOS DE EFECTIVO SERAN DICTADOS EN PESOS (18.20 CONVERSION)")
                            time.sleep(2)
                            cant=cant*18.20
                            cash=efectivoGASTOS[0]
                            cant=cash-cant
                            efectivoGASTOS[0]=cant
                            time.sleep(2)
                            actualizar_valor=update_bankE(efectivoGASTOS[0])
                            efectivoGASTOS=[round(efectivoGASTOS, 2) for efectivoGASTOS in efectivoGASTOS]
                            print(f"\n\nNuevo valor de cuenta =" ,efectivoGASTOS,"MXN\n\n")
                            time.sleep(1)
                            break
                if r==3:
                    print("\n\nSALIENDO...")
                    time.sleep(2)
                    break
    elif n!=1 and n!=2:
        print("\n\nSALIENDO...")
        time.sleep(0)
        break
            
                
                
                    
                
                    
                        

                
        
        
        

        
        
        
    
    
    