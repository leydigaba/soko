 class Soko:

    mapa = [] # mapa del juego
    personaje_columna = 2
    personaje_fila = 1

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3,3,3,3,3],
            [3,4,0,1,4,4,4,4,3],
            [3,4,4,1,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3]
        ]

       
    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def movimiento1(self):
        # Donde estaba el persona pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        # Actualiza la posicion del personaje
        self.personaje_columna+=1

    def derecha(self):
        # Movimiento 1: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            
            
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna+1] ==1 and self.mapa[self.personaje_fila][self.personaje_columna+2] ==4:
            print("personaje,caja,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] =1 #se coloco la caja en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna + 1] =0 #se coloco el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna +=1#se actualizo la pocicion del personaje

        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            print("personaje,caja,meta")
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:      
            print("personaje,meta")
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            print("personaje_meta,espacio")
        



    def jugar(self):
        while True:
            # Imprime el mapa
            self.imprimirMapa()
            # Pide al usuario el movimiento
            movimiento = input("Selecciona el movimiento: ")
            # Moverse a la derecha
            if movimiento == 'd':
                self.derecha()

            # Moverse a la izquerda
            if movimiento == 'a':
                # Movimiento 2: [4,0] -> [0,4]
                if self.mapa[self.personaje_fila][self.personaje_columna -1] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
                    # Donde estaba el piso pone al personaje
                    self.mapa[self.personaje_fila][self.personaje_columna -1 ] = 0
                    # Donde estaba el personaje pone el piso
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    # Actualiza la posicion del personaje
                    self.personaje_columna-=1

    




soko = Soko()
soko.jugar()
