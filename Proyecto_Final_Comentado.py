#IMPORTAR

import pandas as pd
import random
import threading
import time

# FUNCIONES

def idioma_y_nivel(base1):
    idioma=''
    nivel = 0
    vidas=0
    opciones = ''
    
    while True:
    # Siclo para poder romper si el usuario se equivoca en la digitación 
      print("Ingrese el idioma en que quiera jugar")
      idioma = input("Ingrese 'español', 'inglés', 'francés' o 'alemán': ")
      idioma = idioma.lower()

       #Permite que el usuario se equivoque al a la hora de ingresar el idioma 

      if idioma not in ["español", "espanol", "inglés", "ingles", "francés", "frances", "alemán", "aleman"]:
        print("Idioma no válido, por favor inténtelo nuevamente")

      else:
        # Pide el ingreso de niveles dependiendo de el idioma escogido 
        
        if idioma == "español" or idioma =="espanol":
        #Ingreso de datos en español
          print("Ingrese el nivel")
          nivel = int(input("Ingrese '1' para: principiante, '2' para: intermedio o '3' para: avanzado: "))

          if nivel not in [1, 2, 3]:

            print("El nivel no es válido, por favor inténtelo nuevamente")
            continue

          vidas = int(input("Ahora ingrese la cantidad de vidas que desea tener: \n Fácil: 15 \n Intermedio: 10 \n Difícil: 5 \n "))

          if vidas not in [15, 10, 5]:
            print("El número no es válido, por favor inténtelo nuevamente")
            continue

          opciones = base1[f'Palabra Español Nivel {nivel}'].unique()
          print("""  _____                                  _                                 _
 / ___ \                                (_)                               | |
| |   | |_   _  ____     ____ ___  ____  _  ____ ____   ____ ____     ____| |
| |   |_| | | |/ _  )   / ___) _ \|    \| |/ _  )  _ \ / ___) _  )   / _  ) |
 \ \____| |_| ( (/ /   ( (__| |_| | | | | ( (/ /| | | ( (__( (/ /   ( (/ /| |
  \_____)\____|\____)   \____)___/|_|_|_|_|\____)_| |_|\____)____)   \____)_|

   _
  (_)
   _ _   _  ____ ____  ___
  | | | | |/ _  ) _  |/ _ 
  | | |_| ( (/ ( ( | | |_| |
 _| |\____|\____)_|| |\___/
(__/           (_____|                                                       """)


        elif idioma == "inglés" or idioma =="ingles":
        #Ingreso de datos en inglés
          print("Enter level")
          nivel = int(input("Enter '1' for: beginner, '2' for: intermediate or '3' for: advanced: "))

          if nivel not in [1, 2, 3]:
            print("The level is invalid, please try again")
            continue

          vidas = int(input("Now enter the amount of lives that you want to have: \n Easy: 15 \n Intermediate: 10 \n Hard: 5 \n "))

          if vidas not in [15, 10, 5]:

            print("The number is not valid, please try again")
            continue

          opciones = base1[f'Palabra Inglés Nivel {nivel}'].unique()
          print(""" _                         _
| |           _       _   | |
| |      ____| |_    | |_ | | _   ____     ____  ____ ____   ____
| |     / _  )  _)   |  _)| || \ / _  )   / _  |/ _  |    \ / _  )
| |____( (/ /| |__   | |__| | | ( (/ /   ( ( | ( ( | | | | ( (/ /
|_______)____)\___)   \___)_| |_|\____)   \_|| |\_||_|_|_|_|\____)
                                         (_____|
 _                _
| |              (_)
| | _   ____ ____ _ ____
| || \ / _  ) _  | |  _ 
| |_) | (/ ( ( | | | | | |
|____/ \____)_|| |_|_| |_|
           (_____|                                                """)

        elif idioma == "francés" or idioma =="frances":
        #Ingreso de datos en francés
          print("Entrez le niveau")
          nivel = int(input("Entrez '1' pour: débutant, '2' pour: intermédiaire ou '3' pour: avancé: "))

          if nivel not in [1, 2, 3]:

            print("Le niveau n'est pas valide, veuillez réessayer")
            continue

          vidas = int(input("Entrez maintenant le nombre de vies que vous souhaitez avoir: \n Facile: 15 \n Intermédiaire: 10 \n Difficile: 5 \n "))

          if vidas not in [15, 10, 5]:

            print("Le numéro n'est pas valide, veuillez réessayer")
            continue

          opciones = base1[f'Palabra Francés Nivel {nivel}'].unique()
          print("""  _____                 _            _
 / ___ \               | |          (_)
| |   | |_   _  ____   | | ____      _  ____ _   _
| |   |_| | | |/ _  )  | |/ _  )    | |/ _  ) | | |
 \ \____| |_| ( (/ /   | ( (/ /     | ( (/ /| |_| |
  \_____)\____|\____)  |_|\____)   _| |\____)\____|
                                  (__/


  ____ ___  ____  ____   ____ ____   ____ ____
 / ___) _ \|    \|    \ / _  )  _ \ / ___) _  )
( (__| |_| | | | | | | ( (/ /| | | ( (__( (/ /
 \____)___/|_|_|_|_|_|_|\____)_| |_|\____)____)    """)

        elif idioma == "alemán" or idioma =="aleman":
        #Ingreso de datos en Alemán 
          print("Ebene eingeben")
          nivel = int(input("Geben Sie '1' für: anfänger, '2' für: mittelstufe, oder '3' für: fortgeschrittene ein:"))

          if nivel not in [1, 2, 3]:

            print("Level ist ungültig, bitte versuchen Sie es erneut")
            continue

          vidas = int(input("Geben Sie nun die Anzahl der Leben ein, die Sie haben möchten: \n Leicht: 15 \n Mittel: 10 \n Schwer: 5 \n"))

          if vidas not in [15, 10, 5]:

            print("Die Nummer ist ungültig. Bitte versuchen Sie es erneut")
            continue

          opciones = base1[f'Palabra Alemán Nivel {nivel}'].unique()
          print(""" _                                    _                ______       _       _  
(_)                        _         | |              / _____)     (_)     | | 
 _       _____  ___  ___ _| |_     __| |_____  ___   ( (____  ____  _ _____| | 
| |     (____ |/___)/___|_   _)   / _  (____ |/___)   \____ \|  _ \| | ___ | | 
| |_____/ ___ |___ |___ | | |_   ( (_| / ___ |___ |   _____) ) |_| | | ____| | 
|_______)_____(___/(___/   \__)   \____\_____(___/   (______/|  __/|_|_____)\_)
                                                             |_|               
 _                 _                                                           
| |               (_)                                                          
| |__  _____  ____ _ ____  ____  _____ ____                                    
|  _ \| ___ |/ _  | |  _ \|  _ \| ___ |  _ \                                   
| |_) ) ____( (_| | | | | | | | | ____| | | |                                  
|____/|_____)\___ |_|_| |_|_| |_|_____)_| |_|                                  
            (_____|                                                            """)

        print("\n")

        return idioma, vidas, opciones, nivel
        #Retorna las variables necesarias para al proxima función
        break

def rayas_dibujar(idioma, vidas, opciones):
    vidas_orj = vidas # Variable en la que no se alteran las vidas escogidas al inicio 
    aleatorio = random.choice(opciones) # Selección de la palabra 
    palabra = aleatorio.lower() # Justificar la palabra 
    print(palabra)#Borrar después
    letras_ingresadas=[]
    start_time = time.time()
    if idioma == "español":
        print("La palabra tiene " + str(len(palabra)) + " letras")
    elif idioma == "inglés":
        print("The word has " + str(len(palabra)) + " letters")
    elif idioma == "francés":
        print("Le mot a " + str(len(palabra)) + " lettres")
    elif idioma == "alemán":
        print("Das Wort hat " + str(len(palabra)) + " Buchstaben")

    rayas = "-" * len(palabra)
    while vidas > 0:
        imprimir_ahorcado(vidas)
        print(rayas)
        print(" ")
        let: str = input("Ingrese una letra: " if idioma == "español" else "Enter a letter: " if idioma == "inglés" else "Entrez une lettre: " if idioma == "francés" else "Geben Sie einen Buchstaben ein: " )
        while len(let) !=1 or 0<= ord(let)<=64 or 91<= ord(let)<=96 or ord(let)>=123  : # El usuario puede equivocarse e ingresar un caracter diferente a una letra
           #Si el ASCII del caracter no es de una letra mínuscula o mayúscula:   
            let:str=input("Cracter invalido, intentelo de nuevo: " if idioma == "español" else "Invalid character, try again: " if idioma == "inglés" else "Caractère invalide, réessayez: " if idioma == "francés" else "Geben Sie einen Buchstaben ein: " )
        letra = let.lower() # El usuario puede ingresar letras también en mayúscula 
        if letra in letras_ingresadas:
            print("Ya ingresaste esa letra, ingresa otra " if idioma=="español" else "You already entered that letter, enter another" if idioma =="inglés" else "Vous avez déjà entré cette lettre, entrez un autre" if idioma=="francés" else "Sie haben diesen Buchstaben bereits eingegeben. Geben Sie einen anderen ein")
        else: 
          letras_ingresadas.append(letra) #Si la letra no ha sido ingresada se agrega a una lista 
          if letra in palabra:
              for i in range(len(palabra)): 
                  if palabra[i] == letra: # Determinar posición de la letra 
                      rayas = rayas[:i] + letra + rayas[i + 1:]
                      # Dijbuar rayas antes de la posición de la letra y depués de la posición de la letra
          else:
            vidas -= 1
            if vidas != 0:
                #Si se pierde una vida se avisa cunatas quedan 
                print(f"Te quedan {vidas} vidas" if idioma == "español" else f"You have left {vidas} lives" if idioma == "inglés" else f"Il te reste {vidas} vies" if idioma=="francés" else f"Du hast noch {vidas} Leben übrig")
            else:
                #Aviso de perder según el idioma 
                print("Te quedaste sin vidas, vuélvelo a intentar" if idioma == "español" else "You ran out of lives, try again" if idioma == "inglés" else "Tu as manqué de vies, réessaie" if idioma == 'francés' else "")
                print("""                      
                       ____
                      |   |
                     \O/  |
                      |   |
                     / \  |
                    ______|

          """)
                if idioma == "español" or idioma =="espanol":
                   print(""" ______               _ _                       __ 
(_____ \             | (_)     _               / _)
 _____) )___  ____ _ | |_  ___| |_  ____    _ / /  
|  ____/ _  )/ ___) || | |/___)  _)/ _  )  (_| (   
| |   ( (/ /| |  ( (_| | |___ | |_( (/ /    _ \ \_ 
|_|    \____)_|   \____|_(___/ \___)____)  (_) \__)""")
                elif  idioma == "inglés" or idioma =="ingles":
                   print(""" _     _              _                         __ 
| |   | |            | |                       / _)
| |___| |__  _   _   | | ___   ___  ____    _ / /  
 \_____/ _ \| | | |  | |/ _ \ /___)/ _  )  (_| (   
   ___| |_| | |_| |  | | |_| |___ ( (/ /    _ \ \_ 
  (___)\___/ \____|  |_|\___/(___/ \____)  (_) \__)""")
                elif idioma == "francés" or idioma =="frances":
                   print(""" _______                                            _              __ 
(_______)                                          | |            / _)
 _      _   _     ____  ___    ____   ____  ____ _ | |_   _    _ / /  
| |    | | | |   / _  |/___)  |  _ \ / _  )/ ___) || | | | |  (_| (   
| |____| |_| |  ( ( | |___ |  | | | ( (/ /| |  ( (_| | |_| |   _ \ \_ 
 \______)____|   \_||_(___/   | ||_/ \____)_|   \____|\____|  (_) \__)
                              |_|                                     """)
                elif idioma == "alemán" or idioma =="aleman":
                   print(""" ______                             _  _                             _ 
(______)                           | |(_)                  _        / )
 _     _ _   _    _   _ _____  ____| | _ _____  ____ ___ _| |_    _| | 
| |   | | | | |  | | | | ___ |/ ___) || | ___ |/ ___)___|_   _)  (_) | 
| |__/ /| |_| |   \ V /| ____| |   | || | ____| |  |___ | | |_    _| | 
|_____/ |____/     \_/ |_____)_|    \_)_|_____)_|  (___/   \__)  (_)\_)""")
    
        if (rayas.strip("-"))==palabra:
          print(palabra)
          if idioma == "español" or idioma =="espanol":
             print("""  _______                                       _ 
 (_______)                         _           | |
  _   ___ _____ ____  _____  ___ _| |_ _____   | |
 | | (_  (____ |  _ \(____ |/___|_   _) ___ |  |_|
 | |___) / ___ | | | / ___ |___ | | |_| ____|   _ 
  \_____/\_____|_| |_\_____(___/   \__)_____)  |_|""")
          
          elif  idioma == "inglés" or idioma =="ingles":
             print(""" _     _                      _       _ 
| |   | |                    (_)     | |
| |___| | ___  _   _    _ _ _ _ ____ | |
|_____  |/ _ \| | | |  | | | | |  _ \|_|
 _____| | |_| | |_| |  | | | | | | | |_ 
(_______|\___/|____/    \___/|_|_| |_|_|""")
          elif idioma == "francés" or idioma =="frances":
             print(""" _     _                                                        _ 
(_)   (_)                                                      | |
 _     _ ___  _   _  ___     ____ _____  ____ ____  _____ _____| |
| |   | / _ \| | | |/___)   / _  (____ |/ _  |  _ \| ___ (___  )_|
 \ \ / / |_| | |_| |___ |  ( (_| / ___ ( (_| | | | | ____|/ __/ _ 
  \___/ \___/|____/(___/    \___ \_____|\___ |_| |_|_____|_____)_|
                           (_____|     (_____|                    """)
          elif  idioma == "alemán" or idioma =="aleman":
             print("""     _                            _                        _ 
    | |                          (_)                   _  | |
  __| |_   _     ____ _____ _ _ _ _ ____  ____   ___ _| |_| |
 / _  | | | |   / _  | ___ | | | | |  _ \|  _ \ /___|_   _)_|
( (_| | |_| |  ( (_| | ____| | | | | | | | | | |___ | | |_ _ 
 \____|____/    \___ |_____)\___/|_|_| |_|_| |_(___/   \__)_|
               (_____|                                       """)
        
        
          break
    return start_time, vidas, vidas_orj
          
          
             


def imprimir_ahorcado(vidas):
    if vidas == 1:
        print("""
                       ___
                      |   |
                     \O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif vidas == 2:
        print("""
                       ___
                      |   |
                     \O/  |
                      |   |
                          |
                    ______|
        """)
    elif vidas == 3:
        print("""
                       ___
                      |   |
                     \O/  |
                          |
                          |
                    ______|
        """)
    elif vidas == 4:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
#NIVEL DIFICIL
    elif vidas == 5:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)
    elif vidas == 6:
        print("""
                       ___
                      |   |
                          |
                          |
                          |
                    ______|
        """)
    elif vidas == 7:
        print("""
                       ___
                          |
                          |
                          |
                          |
                    ______|
        """)
    elif vidas == 8:
        print("""

                          |
                          |
                          |
                          |
                    ______|
        """)
    elif vidas == 9:
        print("""


                          |
                          |
                          |
                    ______|
        """)
    elif vidas == 10:
        print("""



                          |
                          |
                    ______|
        """)
    elif vidas == 9:
        print("""




                          |
                    ______|
        """)
#NIVEL MEDIO
    elif vidas == 10:
        print("""





                    ______|
        """)
    elif vidas == 11:
        print("""





                    ______
        """)
    elif vidas == 12:
        print("""





                    _____
        """)
    elif vidas == 13:
        print("""





                    ____
        """)
    elif vidas == 14:
        print("""





                    ___
        """)
#NIVEL FACIL
    elif vidas == 15:
        print("""





                    __
        """)

def puntaje(start_time, idioma, vidas_orj, nivel, vidas):
 
    end_time = time.time() #Finalizar cronometro 
    elapsed_time = end_time - start_time #Se halla el tiempo total 
    puntaje_base: int = 0
    puntaje_vidas:int = 0
    if nivel == 1:
        puntaje_base = 100                       #Se define el puntaje base para el nivel 1
        if vidas_orj==5:
            puntaje_vidas = 10 * (5 - vidas)     #Calcula las vidas que se gastaron
        elif vidas_orj==10:
            puntaje_vidas = 10 * (10 - vidas)    #Calcula las vidas que se gastaron
        elif vidas_orj==15:
            puntaje_vidas = 10 * (15 - vidas)    #Calcula las vidas que se gastaron

    elif nivel == 2:
        puntaje_base = 150                       #Se define el puntaje base para el nivel 2
        if vidas_orj==5:
            puntaje_vidas = 10 * (5 - vidas)     #Calcula las vidas que se gastaron
        elif vidas_orj==10:
            puntaje_vidas = 10 * (10 - vidas)    #Calcula las vidas que se gastaron
        elif vidas_orj==15:
            puntaje_vidas = 10 * (15 - vidas)    #Calcula las vidas que se gastaron

    elif vidas_orj == 3:
        puntaje_base = 200                       #Se define el puntaje base para el nivel 3
        if vidas_orj==5:
            puntaje_vidas = 10 * (5 - vidas)     #Calcula las vidas que se gastaron
        elif vidas_orj==10:
            puntaje_vidas = 10 * (10 - vidas)    #Calcula las vidas que se gastaron
        elif vidas_orj==15:
            puntaje_vidas = 10 * (15 - vidas)    #Calcula las vidas que se gastaron

    puntaje_final = 10000 - (elapsed_time * puntaje_base) - puntaje_vidas   #En esta podemos observar que el puntaje máximo será 10.000 y a este valor se le restará:
                                                                            #La multiplicación del tiempo que se demoró en adivinar la palabra por el puntaje base (elapsed_time * puntaje_base)
                                                                            #El puntaje que obtuvo según la cantidad de vidas restantes

    return puntaje_final

def fin_partida(puntaje_final, idioma):

  if idioma=="español" or idioma =="espanol":

    print("\n")
    print("¡Obtuviste un puntaje de: " + str(puntaje_final) +"!")           #Se muestra el puntaje final obtenido
    print("\n")

    if puntaje_final<=3333:                                                 #Desempeño bajo y su mensaje correspondiente
      print(":( sigue prácticando)")              

    if puntaje_final>3333 and puntaje_final<6666:                           #Desempeño medio y su mensaje correspondiente
      print("¡Buen trabajo, sigue prácticando para convertirte en maestro ;)")

    if puntaje_final>=6666:                                                 #Desempeño alto y su mensaje correspondiente
      print("¡Excelente, eres todo un maestro :)")

      #Lo mismo que el código anterior pero en inglés

  if idioma=="inglés" or idioma =="ingles":

    print("\n")
    print("¡You got a score of: " + str(puntaje_final) +"!")
    print("\n")

    if puntaje_final<=3333:
      print(":( keep practicing)")

    if puntaje_final>3333 and puntaje_final<6666:
      print("¡Good job, keep practicing to become a master ;)")

    if puntaje_final>=6666:
      print("¡Excellent, you are a master :)")

      #Lo mismo que el código anterior pero en francés

  if idioma=="francés" or idioma =="frances":

    print("\n")
    print("¡Vous avez un score de: " + str(puntaje_final) +"!")
    print("\n")

    if puntaje_final<=3333:
      print(":( continue pratiquant)")

    if puntaje_final>3333 and puntaje_final<6666:
      print("¡Bon travail, continuez à pratiquer pour devenir un maître ;)")

    if puntaje_final>=6666:
      print("¡Excellent, tu es un maître :)")

      #Lo mismo que el código anterior pero en alemán

  if idioma=="alemán" or idioma =="aleman":

    print("\n")
    print("¡Du hast eine Punktzahl von: " + str(puntaje_final) +"!")
    print("\n")

    if puntaje_final<=3333:
      print(":( Übe weiter)")

    if puntaje_final>3333 and puntaje_final<6666:
      print("¡Gute Arbeit, übe weiter, um ein Meister zu werden ;)")

    if puntaje_final>=6666:
      print("¡Ausgezeichnet, du bist ein Meister :)")

def Jugar_1():
    base1 = pd.read_csv('C:\Base de Datos.csv')                   #Se abre la base de datos en formato csv
    print("------------------------------------------------------------------------------------------------------------")

    #Se llaman y se definen las variables que retorna cada función

    idioma, vidas, opciones, nivel = idioma_y_nivel(base1)
    start_time, vidas, vidas_orj=rayas_dibujar(idioma, vidas, opciones)
    puntaje_final=puntaje(start_time, idioma, vidas, nivel, vidas_orj)
    if vidas != 0:
        fin_partida(puntaje_final, idioma)

#Juego de dos personas con las mismas características 
def Jugar_2(idioma, nivel, opciones, vidas):
    start_time, vidas, vidas_orj = rayas_dibujar(idioma, vidas, opciones)
    puntaje_final = puntaje(start_time, idioma, vidas, nivel, vidas_orj)
    if vidas != 0:
        fin_partida(puntaje_final, idioma)

def Simultaneo():
    base1 = pd.read_csv('C:\Base de Datos.csv')
    print("------------------------------------------------------------------------------------------------------------")
    idioma, vidas, opciones, nivel = idioma_y_nivel(base1)

    # Crear dos hilos para que dos jugadores jueguen simultáneamente
    t1 = threading.Thread(target=Jugar_2, args=(idioma, nivel, opciones, vidas))
    t2 = threading.Thread(target=Jugar_2, args=(idioma, nivel, opciones, vidas))

    t1.start()
    t2.start()
    # Esperar a que el hilo termine antes de continuar con el programa principal
    t1.join()
    t2.join()

Jugadores = int(input("Ingrese la cantidad de jugadores (1 o 2): "))
if Jugadores != 2 and Jugadores != 1:
    Jugadores = int(input("Cantidad de jugadores no válida, inténtalo de nuevo: "))
else:
    Jugadores = Jugadores

if __name__ == "__main__":
    if Jugadores == 1:
        Jugar_1()
    elif Jugadores == 2:
        Simultaneo()

