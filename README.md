# AhorcaPartyChallenge

**Un proyecto lleno frustraciones y alegrías, pero sobre todo enseñanzas.** 

**By Fotocopiadora Alejas²**

![Logo](https://github.com/mvarelau/AhorcaPartyChallenge/assets/141885396/c92c3d58-f7b8-457c-92c4-595a98108c1b)

## Planeación
En un principio tuvimos que organizar los pasos que ibamos a seguir y las posibilidades que teníamos para hacer el juego un poco más complejo. Lo plasmamos en el siguiente cuadro: 
![image](https://github.com/mvarelau/AhorcaPartyChallenge/assets/141885396/c967ae9d-e624-432f-a007-9690e3f82a9a)
A partir de este cuadro empezamos a tomar decisiones: 
* Definitivamente hariamos que el juego tuviera capacidad para tres idimomas diferentes ( que terminaron siendo 4)
* Al finalizar la parte lógica del juego evaluaríamos la posibilidad de manejar puntajes.
* El juego podría jugarse simultaneamente por dos personas.
 ## Realización
### Base de datos 
* Aún no sabiamos manejo de archivos más allá de drive en colab así que nos decidimos por lo conocido. Creamos un archivo en formato CSV en el que guardamos las más de 4000 palabras en los idiomas español, inglés, francés, y alemán. Cada idioma con su respectiva dificultada dada por la cantidad de letras. Aquí un pequeño fragmento: 
![image](https://github.com/mvarelau/AhorcaPartyChallenge/assets/141885396/80f77f31-6ce6-4dfa-aad7-7d025ab26bc5)

### Preparación (Importar)

Empezamos importando todas las librerías que necesitariamos para que corra el programa:
| | Nombre | Uso |
|-|-------------|-----------------------|
| 1 | Pandas | Importar nuestra base de datos |
| 2 | Random | Seleccionar la palabra a adivinar |
| 3 | threading | PARA QUE¿? |
| 4 | time | Cronometrar el tiempo que se demora el usuario en adivinar la palabra |

```python
import pandas as pd
import random
import threading
import time
```

### Preparación (Función idioma y nivel)

Empezamos programando la preparación del juego, es decir las posibilidades que tendría el jugador para un juego más dinamico.

Lo primero que hicimos fue definir nuestras variables: idioma, nivel, vidas y opciones. El programa decidimos introducirlo en un **while** para asegurarnos de que el usuario ingrese únicamente las opciones que tenemos contempladas, en caso de ser diferente las preguntas se volverán a realizar hasta que el usuario lea y siga de manera correcta el enunciado.

   - Idioma:\
     Después de haber sido escogido, el resto del juego se ejecutaria en este idioma, lo que quería decir que cada outpout debía tener los cuatro idiomas. 
   - Dificultad por palabra:\
      Esto determinaría el grupo en el que la función random se movería 
   - Dificultad por vidas (Los intentos fallidos en los que se dibujaría por completo el muñeco)
```python
def idioma_y_nivel(base1):
    idioma=''
    nivel = 0
    vidas=0
    opciones = ''
    
    while True:

      print("Ingrese el idioma en que quiera jugar")
      idioma = input("Ingrese 'español', 'inglés', 'francés' o 'alemán': ")
      idioma = idioma.lower()

      if idioma not in ["español", "espanol", "inglés", "ingles", "francés", "frances", "alemán", "aleman"]:
        print("Idioma no válido, por favor inténtelo nuevamente")

      else:

        if idioma == "español" or idioma =="espanol":

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

        break
```
Para que el juego se viera un poco más amistoso decidimos usar ASCII art, "El arte ASCII es cualquier tipo de imagen o diagrama dibujado con caracteres imprimibles en el juego de caracteres ASCII" Según la pagina de ASCII art que utilizamos:\
https://www.asciiart.eu/faq
### Dibujos
En un principio lo que hicimos fue crear la función que dibujaría el muñeco teniendo en cuenta la cantidad de vidas. Este pequeño lo dibujamos en 15 pasos que sería el máximo de vidas. Con un condicional if-elif le dimos a cada vida una progresión de muñecos que se contruyen de a poco. Vale mencionar que utilizamos una triple comilla en el print tanto de él muñeco como del ASCII art, esto permite que se imprima exactamente lo que se escribe así tenga espacios o saltos de línea sin la necesidad de un script determinado.
```python
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
```
### Lógica 
Ya teniendo el muñeco hecho podiamos crear la función "Motor" del juego, está función sería la que evaluaría las letras que ingresa el usuario, y con el resultado de ese análisis se imprimiría las lineas con la letra adivinada, si era el caso, en su posición determinada y si no, se encargaría de restar un vida y dibujar el correspondiente muñeco.
* Lo primero es ecoger una palabra y asignarla a una variable, posteriormente se dibujan las lineas correspondientes a la cantidad de caracteres ( Nos hubiera gustado que las lineas fueran un poco más largas, y no solo un guión, pero como trabajaríamos con la función ```len``` decidimos que era más práctico)
* El ciclo while se hizo con la condición de que las vidas fueran mayores a 0. En cada una de las iteraciones del juego se imprime el muñeco, las líneas y se le pide al usuario ingresar una letra, más adelante se evalúa si esta letra ya fue ingresada antes, esto se hace gracias a una lista vacía a la que se van agregando los elementos que el usuario ingresa, si el elemento resulta estar en la lista, se pedirá al usuario ingresar una letra diferente, en el caso de no estar, se examina si hace parte de la palabra, si hace parte entonces se valora en que posición está, y por último con ayuda de un *slicing* se dibujan la lineas hasta antes de la posición de la letra, la letra, y las lineas sobreantes después de la posición de la letra.
```python
def rayas_dibujar(idioma, vidas, opciones):
    aleatorio = random.choice(opciones)
    palabra = aleatorio.lower()
    letras_ingresadas=[]
    if idioma == "español":
        print("La palabra tiene " + str(len(palabra)) + " letras")
    elif idioma == "inglés":
        print("The word has " + str(len(palabra)) + " letters")
    elif idioma == "francés":
        print("Le mot a " + str(len(palabra)) + " lettres")

    rayas = "-" * len(palabra)
    while vidas > 0:
        imprimir_ahorcado(vidas)
        print(rayas)
        print(" ")
        letra: str = input("Ingrese una letra: " if idioma == "español" else "Enter a letter: " if idioma == "inglés" else "Entrez une lettre: ")
        
        if letra in letras_ingresadas:
            print("Ya ingresaste esa letra, ingresa otra " if idioma=="español" else "You already entered that letter, enter another" if idioma =="inglés" else "Vous avez déjà entré cette lettre, entrez un autre")
        else: 
          letras_ingresadas.append(letra)
          if letra in palabra:
              for i in range(len(palabra)):
                  if palabra[i] == letra:
                      rayas = rayas[:i] + letra + rayas[i + 1:]
```
* De no cumplirse que la letra esté en la palabra se resta una vida, si el usuario aún cuenta con vidas, el juego le notificará cuantas le quedan, pero si por el contrario el usuario ya no cuenta con vidas, el programá le dirá que perdió y se cerrará el rpograma.
```python
else:
              vidas -= 1
              if vidas != 0:
                  print(f"Te quedan {vidas} vidas" if idioma == "español" else f"You have left {vidas} lives" if idioma == "inglés" else f"Il te reste {vidas} vies")
              else:
                  print(f"Te quedaste sin vidas, vuélvelo a intentar" if idioma == "español" else f"You ran out of lives, try again" if idioma == "inglés" else f"Tu as manqué de vies, réessaie")
                  print("""
                       ___
                      |   |
                     \O/  |
                      |   |
                     / \  |
                    ______|
          """)
                  if idioma=='español':
                    print(""" ______               _ _                       __ 
(_____ \             | (_)     _               / _)
 _____) )___  ____ _ | |_  ___| |_  ____    _ / /  
|  ____/ _  )/ ___) || | |/___)  _)/ _  )  (_| (   
| |   ( (/ /| |  ( (_| | |___ | |_( (/ /    _ \ \_ 
|_|    \____)_|   \____|_(___/ \___)____)  (_) \__)""")
                  if idioma == "inglés":
                    print(""" _     _              _                         __ 
| |   | |            | |                       / _)
| |___| |__  _   _   | | ___   ___  ____    _ / /  
 \_____/ _ \| | | |  | |/ _ \ /___)/ _  )  (_| (   
   ___| |_| | |_| |  | | |_| |___ ( (/ /    _ \ \_ 
  (___)\___/ \____|  |_|\___/(___/ \____)  (_) \__)""")
                  if idioma =="francés":
                    print(""" _______                                            _              __ 
(_______)                                          | |            / _)
 _      _   _     ____  ___    ____   ____  ____ _ | |_   _    _ / /  
| |    | | | |   / _  |/___)  |  _ \ / _  )/ ___) || | | | |  (_| (   
| |____| |_| |  ( ( | |___ |  | | | ( (/ /| |  ( (_| | |_| |   _ \ \_ 
 \______)____|   \_||_(___/   | ||_/ \____)_|   \____|\____|  (_) \__)
                              |_|                                     """)
```
* ¡Listo, el juego se ejecuta perfectamente, el usuario puede decidir en que modalidad jugar, y las iteraciones se hacen correctamente! ¿Ahora qué? Bueno, sería bastante genial competir con un amigo.\
Descubrimos que existe una librería llamda ```threading``` que permite la creación y gestión de hilos. Los hilos son unidades de ejecución independientes que permiten que un programa realice múltiples tareas simultáneamente. Al utilizar la clase Thread, se pueden crear y controlar hilos, cada uno ejecutando funciones específicas. Sin embargo, tuvimos algunos problemas ya que es crucial considerar la sincronización y los problemas de concurrencia al acceder a datos compartidos entre hilos, algo que evidentemente pordia ocurrir cuando los hilos que queríamos manejar eran de la misma función.













