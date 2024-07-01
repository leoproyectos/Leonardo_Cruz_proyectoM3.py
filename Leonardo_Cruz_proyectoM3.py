#Tenemos que importar random para poder hacer la maquina de galton aleatoria
import random

#Luego tenemos que hacer una funcion para la maquina de galton la cual va a contener los niveles y las pelotas que vamos a utilizar
def galton(levels, balls):
#El for va a servir para poder decirle al programa cuantas pelotas vamos a tener, asi vamos a ir bola por bola hasta que termine el programa
    for ball in range(1, balls+1):
        indx = 0
#Aqui vamos a definir los niveles que va a tener nuestra maquina de galton
        for level in range(levels):
            print(f"Ball:{ball}, Level:{levels}")
#Aqui vamos a definir los movientos de forma aleatoria
            next_move = random.choice([-1, 1])
            if next_move == -1:
                print("Siguiente movimiento es izquierda")
            elif next_move == 1:
                indx = indx + 1
                print("Siguiente movimiento es derecha")


if __name__ == "__main__":
    galton(12, 3000)
