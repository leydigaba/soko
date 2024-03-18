class Soko:

    mapa = [] # mapa del juego
    personaje_columna = 2
    personaje_fila = 1

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3,3,3,3,3],
            [3,4,0,1,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3]
        ]

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def derecha(self):
        # Movimiento 5: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            print("personaje,pasillo")
            self.mapa[self.personaje_fila][self.personaje_columna +1 ] = 0 #se coloca el personaje en la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna +=1 #se actualiza la posicion del personaje

        #Moviento 6: [0,2]  ->	[4,5]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            print("personaje,meta")
            self.mapa[self.personaje_fila][self.personaje_columna +1] =5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna +0] =4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna +=1 #se acualizo la posicion del personaje

        #Movimiento 7: [0,1,4]  ->	[4,0,1]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna+1] ==1 and self.mapa[self.personaje_fila][self.personaje_columna+2] ==4:
            print("personaje,caja,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] =1  #se coloco la caja en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna + 1] =0  #se coloco el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna +=1#se actualizo la posicion del personaje

        #Moviento 8: [0,1,2] ->	[4,0,6]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            print("personaje,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 6 #se coloco la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 0 #se coloca el personaje en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna +0] = 4 #se coloco el espacio en donde estaba el personaje
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            
        #Moviemiento 9:  [0,6,4] -> [4,5,1] 
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna +1] ==6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            print("Personaje, caja_meta, pasillo")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 #se coloco la caja en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna +1 ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna +0 ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            
        #Movimiento 10:  [0,6,2] -> [4,5,6] 
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna +1] ==6 and self.mapa[self.personaje_fila ][self.personaje_columna +2] ==2:
            print("Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna +2 ] = 6 #se coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 4 #donde estaba el personaje se coloco un espacio
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            
        #Movimiento 11: [5,4] -> [2,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 4:
            print("Personaje_meta, pasillo")
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 0 #se coloca el personaje en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna +0] = 2 #donde estabe personaje_meta se coloco una meta
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            
        #Movimiento 12: [5,2] -> [2,5]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna +1] ==2:
            print("Personaje_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            
        #Movimiento 13: [5,1,4] -> [2,0,1]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna +1]== 1 and self.mapa[self.personaje_fila][self.personaje_columna +2] == 4:
            print("Personaje_meta, caja, pasillo")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 #se coloca la caja en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            
        #Movimiento 14: [5,1,2] -> [2,0,6]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna +2] ==2:
            print("Personaje_meta, caja, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 #se coloca la caja en donde esta la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna +=1 #se actualiza la posicion del personaje
            
        #Movimiento 15 :[5,6,4] -> [2,5,1]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna +2] ==4:
            print("Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 #se coloca la caja en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna +=1 #se actualiza la posicion del personaje
            
        #Movimiento 16:
        
         #Movimiento 15 : [5,6,2] -> [2,5,6]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna +2] ==2:
            print("Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 #se coloca la caja_meta en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna +=1 #se actualiza la posicion del personaje
             

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
