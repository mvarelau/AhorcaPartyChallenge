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

### Importar

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
COPIAR FUNCIÓN YA LISTA
```

### Función Rayas palabra incógnita

Nuestra segunda función es la función **"motor"** del juego, ya que en torno a está funciona la mayoría del sentido del juego. Por una parte, se inicia el conteo de tiempo de juego (para en un futuro establecer el puntaje del usuario) usando **time¨**. 

Por otra parte, haciendo uso de la función **len** se establece el largo de la palabra seleccionada por el programa y, se imprime un mensaje para que el usuario sepa la cantidad de letras que contiene la palabra y además, se muestra en pantallas las líneas que representan cada caracter que se debe adivinar. Nos hubiera gustado que las lineas fueran un poco más largas, y no solo un guión, pero como trabajaríamos con la función ```len``` decidimos que era más práctico tan solo usar un guión.

Por último, haciendo uso de **while** usamos una condición para que se repita continuamente la solicitud para que el usuario ingrese una letra hasta que se quede sin vidas. Dentro de este, tambien se llama la función donde se imprimirá el avance del ahorcado cada vez que el usuario pierda una vida. Decidimos empatizar con el usuario y, por esta razón, en caso de ingresar una palabra repetida se le informará que repitió la palabra, NO perderá una vida (por distraido) y se le pedirá al usuario ingresar una letra diferente. Cada vez que la palabra ingresada sea correcta, se valora en que posición está, y por último con ayuda de un *slicing* se dibujan la lineas hasta antes de la posición de la letra, la letra, y las lineas sobreantes después de la posición de la letra.

Decidimos incluir dentro de esta misma función por efectos prácticos el diagrama final del ahorcado cuando el usuario se queda sin vidas (y ya no se cumpla el while) y un letrero informando que perdió el juego (en el idioma correspondiente). 

Al final de está función se retornará las variables start_time, vidas (se le irán restando a esta variable cada vez que el usuario pierda una vida) y vidas_orj (una copia de la variable vidas original para usarla en la función de puntaje). Esto para poder usarlas en otras funciones posteriores.

```python
COPIAR FUNCIÓN YA LISTA
```

### Función Dibujo ahorcado

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

### Función Puntaje

Ahora, una de las funciones más esperadas por el usuario...la función que determina el puntaje. Si se corré está función significa que el juego llegó a su final y por está razón el cronometro parará y se calculará el tiempo total que se demoró el usuario en adivinar la palabra. 

* ¡Listo, el juego se ejecuta perfectamente, el usuario puede decidir en que modalidad jugar, y las iteraciones se hacen correctamente! ¿Ahora qué? Bueno, sería bastante genial competir con un amigo.\
Descubrimos que existe una librería llamda ```threading``` que permite la creación y gestión de hilos. Los hilos son unidades de ejecución independientes que permiten que un programa realice múltiples tareas simultáneamente. Al utilizar la clase Thread, se pueden crear y controlar hilos, cada uno ejecutando funciones específicas. Sin embargo, tuvimos algunos problemas ya que es crucial considerar la sincronización y los problemas de concurrencia al acceder a datos compartidos entre hilos, algo que evidentemente pordia ocurrir cuando los hilos que queríamos manejar eran de la misma función.






