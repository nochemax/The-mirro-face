# Crador Smp_A
# Fecha 11.09.2019
# Nombre programa the mirro face
# Tipo phyton3
# Descarga paginas web

import os 
import sys

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  variables  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

listamenu=["Menu de Opciones:", "1--Nombre web ", "2--Directorio a guardar la web ", "3--start clone web", "4--Exit"]#Menu Princcipal
exit=False
key=0

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Funciones menu $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def menu():

  print("\033[1;31;1m ")
  os.system('figlet ThE MiRroR FaCe')
  print("\033[1;37;1m ")
  print("            "+listamenu[0])
  print("\033[1;37;m ")
  print("            "+listamenu[1])
  print("            "+listamenu[2])
  print("            "+listamenu[3])
  print("            "+listamenu[4])

 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Funciones operativas $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def nombre_web():
  global N_web
  N_web=input(str("introduzca el nombre de la web : "))
  print(N_web)

def ruta():
  global ruta
  ruta=input(str("introduzca la ruta : "))
  print(ruta)

def clone(ruta, N_web):
  print(N_web)
  print(ruta)
  line='wget --mirror --convert-links --page-requisites --no-parent -P '+ruta+' '+N_web
  print(str(line))
  os.system(line)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ loop program $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

while exit==False:
  
  menu()
  key=(int(input("            "+"Select: ")))
  
  if (key==1):
    nombre_web()
  elif (key==2):
    ruta()  
  elif (key==3):
    clone(ruta, N_web)
  elif (key==4):
    exit=True
  
print("\033[1;31;1m ")  
print("Smp_A byTe_Dey_bYte_HackiNg")
print("\033[1;31;m ")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
