# AhorcaPartyChallenge 

***"Un proyecto lleno frustraciones y alegrías, pero sobre todo enseñanzas"***

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
  
![image](https://github.com/mvarelau/AhorcaPartyChallenge/assets/141885396/ed59cf1d-67a1-48db-aa7b-3b897ad60e1e)


### Importar

Empezamos importando todas las librerías que necesitariamos para que corra el programa:

| | Nombre | Uso |
|:-:|:-------------:|:-----------------------:|
| 1 | Pandas | Importar nuestra base de datos |
| 2 | Random | Seleccionar la palabra a adivinar |
| 3 | threading | Ejecutar funciones simultaneamente |
| 4 | time | Cronometrar el tiempo que se demora el usuario en adivinar la palabra |

```python
import pandas as pd
import random
import threading
import time
```

### Función idioma y nivel

Empezamos programando la preparación del juego, es decir las posibilidades que tendría el jugador para un juego más dinamico.

Lo primero que hicimos fue definir nuestras variables: idioma, nivel, vidas y opciones. El programa decidimos introducirlo en un **while** para asegurarnos de que el usuario ingrese únicamente las opciones que tenemos contempladas, en caso de ser diferente las preguntas se volverán a realizar hasta que el usuario lea y siga de manera correcta el enunciado.

   - Idioma:\
     
     El usuario debe escoger entre las opciones: español, inglés, francés o alemán. Después de haber sido escogido el idioma, el resto del juego se ejecutaria en este idioma, esto quiere decir, que realizamos condicionales y outputs especificos por cada idioma.
     
   - Dificultad por palabra:\
     
      El usuario debe escoger entre nivel principiante, intermedio o avanzado. Cada nivel de dificultad está determinado por la cantidad de letras que contiene la palabra (principiante: 0-5; intermedio: 6-10; avanzado: 11-16) escogida de la base de datos. El nivel seleccionado determina la columna de la base de datos en el que la función random se movería y seleccionaría la palabra aleatoria.
     
   - Dificultad por vidas:\
     
     El usuario debe seleccionar si desea contar con 5, 10 o 15 vidas; esto influirá en su puntaje final (teniendo en cuenta tambien el nivel de dificultad) Además, según la cantidad de vidas restantes se irá dibujando el ahorcado.
   - ¡Que inicie el juego!:\
     
     Una vez este determinada cada variable aparecerá un letrero tipo video juego (en el idioma seleccionado) informándole al usuario que comenzará el juego.

```python
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
```

### Función rayas palabra incógnita

Nuestra segunda función es la función **"motor"** del juego, ya que en torno a está funciona la mayoría del sentido del juego. Por una parte, se inicia el conteo de tiempo de juego (para en un futuro establecer el puntaje del usuario) usando **time¨**. 

Por otra parte, haciendo uso de la función **len** se establece el largo de la palabra seleccionada por el programa y, se imprime un mensaje para que el usuario sepa la cantidad de letras que contiene la palabra y además, se muestra en pantallas las líneas que representan cada caracter que se debe adivinar. Nos hubiera gustado que las lineas fueran un poco más largas, y no solo un guión, pero como trabajaríamos con la función ```len``` decidimos que era más práctico tan solo usar un guión.

Por último, haciendo uso de **while** usamos una condición para que se repita continuamente la solicitud para que el usuario ingrese una letra hasta que se quede sin vidas. Dentro de este, tambien se llama la función donde se imprimirá el avance del ahorcado cada vez que el usuario pierda una vida. Decidimos empatizar con el usuario y, por esta razón, en caso de ingresar una palabra repetida se le informará que repitió la palabra, NO perderá una vida (por distraido) y se le pedirá al usuario ingresar una letra diferente. Cada vez que la palabra ingresada sea correcta, se valora en que posición está, y por último con ayuda de un *slicing* se dibujan la lineas hasta antes de la posición de la letra, la letra, y las lineas sobreantes después de la posición de la letra.

Decidimos incluir dentro de esta misma función por efectos prácticos el diagrama final del ahorcado cuando el usuario se queda sin vidas (y ya no se cumpla el while) y un letrero informando que perdió el juego (en el idioma correspondiente). 

Al final de está función se retornará las variables start_time, vidas (se le irán restando a esta variable cada vez que el usuario pierda una vida) y vidas_orj (una copia de la variable vidas original para usarla en la función de puntaje). Esto para poder usarlas en otras funciones posteriores.

```python
def rayas_dibujar(idioma, vidas, opciones):
    vidas_orj=vidas # Variable en la que no se alteran las vidas escogidas al inicio 
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
```

### Función dibujo ahorcado

Para que el juego se viera un poco más amistoso decidimos usar ASCII art, "El arte ASCII es cualquier tipo de imagen o diagrama dibujado con caracteres imprimibles en el juego de caracteres ASCII" Según la pagina de ASCII art que utilizamos:\
https://www.asciiart.eu/faq

En un principio lo que hicimos fue crear la función que dibujaría el muñeco teniendo en cuenta la cantidad de vidas. Este pequeño lo dibujamos en 15 pasos que sería el máximo de vidas. Con un condicional if-elif le dimos a cada vida una progresión de muñecos que se contruyen de a poco. 


Vale mencionar que utilizamos una triple comilla en el print tanto de él muñeco como del ASCII art, esto permite que se imprima exactamente lo que se escribe así tenga espacios o saltos de línea sin la necesidad de un script determinado.

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

### Función puntaje

Ahora, una de las funciones más esperadas por el usuario...la función que determina el puntaje. Si se corré está función significa que el juego llegó a su final y por está razón el cronometro parará y se calculará el tiempo total que se demoró el usuario en adivinar la palabra. 

Para definir el puntaje le dimos un puntaje base según el nivel de dificultad que eligió (ya que en esta clase aprendimos a valor el esfuerzo y actitud) en caso de retarse con el nivel más dificil tendrá un putaje base más alto. Ademas, realizamos una equivalencia de puntaje_vidas que tiene en cuenta la cantidad de vidas seleccionadas (por cada nivel) y las vidas restantes que tiene.

<table>
    <thead>
        <tr>
            <th>Nivel</th>
            <th>Puntaje Base</th>
            <th>Vidas</th>
            <th>Puntaje Vidas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3 align="center">Principiante</td>
            <td rowspan=3 align="center">100</td>
            <td align="center">5</td>
            <td align="center">puntaje_vidas = 10 * (5 - vidas)</td>
        </tr>
        <tr>
            <td align="center">10</td>
            <td align="center">puntaje_vidas = 10 * (10 - vidas)</td>
        </tr>
        <tr>
            <td align="center">15</td>
            <td align="center">puntaje_vidas = 10 * (15 - vidas)</td>
        </tr>
        <tr>
            <td rowspan=3 align="center">Intermedio</td>
            <td rowspan=3 align="center">150</td>
            <td align="center">5</td>
            <td align="center">puntaje_vidas = 10 * (5 - vidas)</td>
        </tr>
        <tr>
            <td align="center">10</td>
            <td align="center">puntaje_vidas = 10 * (10 - vidas)</td>
        </tr>
        <tr>
            <td align="center">15</td>
            <td align="center">puntaje_vidas = 10 * (15 - vidas)</td>
        </tr>
        <tr>
            <td rowspan=3 align="center">Avanzado</td>
            <td rowspan=3 align="center">200</td>
            <td align="center">5</td>
            <td align="center">puntaje_vidas = 10 * (5 - vidas)</td>
        </tr>
        <tr>
            <td align="center">10</td>
            <td align="center">puntaje_vidas = 10 * (10 - vidas)</td>
        </tr>
        <tr>
            <td align="center">15</td>
            <td align="center">puntaje_vidas = 10 * (15 - vidas)</td>
        </tr>
    </tbody>
</table>

Para calcular el puntaje final se realizara el siguiente calculo:

```python
puntaje_final = 10000 - (elapsed_time * puntaje_base) - puntaje_vidas
```

En esta podemos observar que el puntaje máximo será 10.000 y a este valor se le restará: 
 * La multiplicación del tiempo que se demoró en adivinar la palabra por el puntaje base (elapsed_time * puntaje_base)
 * El puntaje que obtuvo según la cantidad de vidas restantes

```python
def puntaje(start_time, idioma, vidas_orj, nivel, vidas):
 
    end_time = time.time() #Finalizar cronometro 
    elapsed_time = end_time - start_time 
    puntaje_base: int = 0
    puntaje_vidas:int = 0
    if nivel == 1:
        puntaje_base = 100
        if vidas_orj==5:
            puntaje_vidas = 10 * (5 - vidas)     # Las vidas q gastaron
        elif vidas_orj==10:
            puntaje_vidas = 10 * (10 - vidas)
        elif vidas_orj==15:
            puntaje_vidas = 10 * (15 - vidas)

    elif nivel == 2:
        puntaje_base = 150
        if vidas_orj==5:
            puntaje_vidas = 10 * (5 - vidas)     # Las vidas q gastaron
        elif vidas_orj==10:
            puntaje_vidas = 10 * (10 - vidas)
        elif vidas_orj==15:
            puntaje_vidas = 10 * (15 - vidas)

    elif vidas_orj == 3:
        puntaje_base = 200
        if vidas_orj==5:
            puntaje_vidas = 10 * (5 - vidas)     # Las vidas q gastaron
        elif vidas_orj==10:
            puntaje_vidas = 10 * (10 - vidas)
        elif vidas_orj==15:
            puntaje_vidas = 10 * (15 - vidas)

    puntaje_final = 10000 - (elapsed_time * puntaje_base) - puntaje_vidas

    return puntaje_final

```

### Función fin partida

En esta función se muestra un mensaje (en el idioma correspondiente) de "motivación" / "felicitaciones" / "sube ego" según el puntaje final que se calculó en la anterior función.

```python
def fin_partida(puntaje_final, idioma):

  if idioma=="español" or idioma =="espanol":

    print("\n")
    print("¡Obtuviste un puntaje de: " + str(puntaje_final) +"!")
    print("\n")

    if puntaje_final<=3333:
      print(":( sigue prácticando)")

    if puntaje_final>3333 and puntaje_final<6666:
      print("¡Buen trabajo, sigue prácticando para convertirte en maestro ;)")

    if puntaje_final>=6666:
      print("¡Excelente, eres todo un maestro :)")

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
```

### Función jugar_1

Esta sería como una función que reemplazaría nuestra función main en un código normal...como decidimos incluir la opción de multijugador fue necesario crear está función. Aquí se importa nuestra base de datos en formato csv (valores separados por comas el cual permite guardar los datos en un formato de tabla estructurada) y se llaman las demás funciones definiendo las variables que se requieran en otras funciones teniendo en cuenta los return de cada una.

```python
def Jugar_1():
    base1 = pd.read_csv('C:\Base de Datos.csv')
    print("------------------------------------------------------------------------------------------------------------")
    idioma, vidas, opciones, nivel = idioma_y_nivel(base1)
    start_time, vidas, vidas_orj=rayas_dibujar(idioma, vidas, opciones)
    puntaje_final=puntaje(start_time, idioma, vidas, nivel, vidas_orj)
    if vidas != 0:
        fin_partida(puntaje_final, idioma)
```

### Función Simultaneo
¡Listo, el juego se ejecuta perfectamente, el usuario puede decidir en que modalidad jugar, y las iteraciones se hacen correctamente! ¿Ahora qué? Bueno, sería bastante genial competir con un amigo.\
 Descubrimos que existe una librería llamda ```threading``` que permite la creación y gestión de hilos. Los hilos son unidades de ejecución independientes que permiten que un programa realice múltiples tareas simultáneamente. Al utilizar la clase Thread, se pueden crear y controlar hilos, cada uno ejecutando funciones específicas. Sin embargo, tuvimos algunos problemas ya que es crucial considerar la sincronización y los problemas de concurrencia al acceder a datos compartidos entre hilos, algo que evidentemente pordia ocurrir cuando los hilos que queríamos manejar eran de la misma función. \
 Decidimos que las condiciones para el juego simultaneo debían ser lás mismas, asi que antes de hacer el llamado a la función simultaneamente creamos una función en la que se hacer llamado a todas las funciones excpto a lo función ```idioma_y_nivel```:
```python
def Jugar_2(idioma,nivel,opciones,vidas):
    start_time, vidas, vidas_orj=rayas_dibujar(idioma, vidas, opciones) 
    puntaje_final=puntaje(start_time, idioma, vidas, nivel, vidas_orj)
    if vidas != 0:
        fin_partida(puntaje_final, idioma)
```
Con eso listo ahora si podiamos hacer el llamdo co la función ```Thread```:
```Python
def Simultaneo():
    base1 = pd.read_csv('C:\Base de Datos.csv')
    print("------------------------------------------------------------------------------------------------------------")
    idioma, vidas, opciones,nivel = idioma_y_nivel(base1)

    
    # Crear dos hilos para que dos jugadores jueguen simultáneamente
    t1 = threading.Thread(target=Jugar_2, args=(idioma, vidas, opciones,nivel))
    t2 = threading.Thread(target=Jugar_2, args=(idioma, vidas, opciones,nivel))

    t1.start()
    t2.start()
    # Esperar a que el hilo termine antes de continuar con el programa principal
    t1.join()
    t2.join()
```
### Definir Jugadores
Se crea una variable en la que el usuario ingresa la cantidad de jugadores que desea, si ingresa un caracter diferente a 1 o 2 se volvera a pedir que lo ingrese.
```python
Jugadores=int(input("Ingrese la cantidad de jugadores (1 o 2): "))
if Jugadores != 2 and Jugadores != 1: 
   Jugadores=int(input("Cantidad de jugadores no válida, intentalo de nuevo: "))
   
else: 
   Jugadores=Jugadores
```
### Función Main 
Teniendo en cuenta la cantidad de jugadores, se hará llamado a la función ```Jugar_1``` o ```Simultaneo```
```python
if __name__=="__main__":
   if Jugadores==1:
      Jugar_1()
   if Jugadores == 2:
      Simultaneo()
```
