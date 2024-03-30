class Soko:

    def __init__(self):
        self.mapa = None
        self.nivel_seleccionado = False

    def seleccionar_nivel(self, nivel):
        if nivel == 1:
            self.mapa = [
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 4, 0, 2, 1, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 4, 4, 4, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3]
            ]
            self.personaje_columna = 2
            self.personaje_fila = 1
            self.nivel_seleccionado = True
        elif nivel == 2:
            # Define el mapa del nivel 2
            self.mapa = [
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 4, 4, 2, 1, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 4, 4, 4, 3],
                [3, 4, 4, 4, 0, 4, 4, 4, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3]
            ]
            self.personaje_columna = 4
            self.personaje_fila = 3
            pass
        elif nivel == 3:
            # Define el mapa del nivel 3
            pass
        else:
            print("Nivel incorrecto. Cerrando el juego.")
            exit()

        # Establece el indicador de nivel seleccionado en Verdadero
        self.nivel_seleccionado = True
        return True

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

    def izquierda(self):
                
        # Movimiento 2: [4,0] -> [0,4]
        if self.mapa[self.personaje_fila][self.personaje_columna -1] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila][self.personaje_columna -1 ] = 0
            # Donde estaba el personaje pone el piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Actualiza la posicion del personaje
            self.personaje_columna-=1
                    
         
        #Movimiento 20 : [2,1,0] -> [6,0,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==2 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 0:
            print("Personaje, caja y meta ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4 #se coloca piso donde estaba el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0 #se coloca personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 6 # donde estaba la meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
        #Movimiento 21 : [4,6,0] -> [1,5,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==4 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 0:
            print("Personaje, caja_meta y espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4 #se coloca espacio donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloca personaje meta donde estabacaja meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 1 #donde estaba espacio se coloca caja
            self.personaje_columna -=1 #se actualiza la posicion del personaje
                        
            
        #Movimiento 22 : [2,6,0] -> [6,5,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==2 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 0:
            print("Personaje, caja_meta y meta ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4 #se coloca espacio en donde estaba persona
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloca personaje meta en donde estaba caja meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 6 #donde estaba meta se coloca una caja meta
            self.personaje_columna *=1 #se actualiza la posicion del personaje
        
        
            #Movimiento 23 : [4,5] -> [0,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==4 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 5:
            print(" Personaje_meta y espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 2 #se coloca meta donde estabapersonaje meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 0 #donde estaba espacio se coloca un personaje
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
                #Movimiento 24 : [2,5] -> [5,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==2 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 5:
            print(" Personaje_meta y meta ")
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 5 #donde estaba meta se coloca un personaje meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
                
        #Movimiento 25 : [4,1,5] -> [1,0,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==4 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 5:
            print("Personaje_meta, caja y espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0 #se coloca personaje en donde estaba caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 1 #donde estaba espacio se coloco la caja
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
        #Movimiento 26 : [2,1,5] -> [6,0,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 5:
            print("Personaje_meta, caja y espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0 #se coloca personaje donde estaba caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 6 #donde estaba meta se caja meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
            
            #Movimiento 27 : [4,6,5] -> [1,5,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 4 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 5:
            print("Personaje_meta, caja y espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloca personaje meta donde estaba caja meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 1 #donde estaba espacio se coloca una caja
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
                        #Movimiento 28 : [2,6,5] -> [6,5,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 5:
            print("Personaje_meta, caja_meta y meta")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2 #se coloca meta en donde estaba personaje meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloca personaje meta donde estaba caja meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 6 #donde estaba meta se coloco una cja
            self.personaje_columna -=1 #se actualiza la posicion del personajea
            
            
            
            
            
            
    def abajo(self):
        
             # Movimiento 5: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna ] == 4:
            print("personaje,pasillo")
            self.mapa[self.personaje_fila +1][self.personaje_columna] = 0 #se coloca el personaje en la caja
            self.mapa[self.personaje_fila +0][self.personaje_columna] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1 #se actualiza la posicion del personaje

        #Moviento 6: [0,2]  ->	[4,5]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna ] == 2:
            print("personaje,meta")
            self.mapa[self.personaje_fila +1][self.personaje_columna] =5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila +0][self.personaje_columna ] =4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1 #se acualizo la posicion del personaje

        #Movimiento 7: [0,1,4]  ->	[4,0,1]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila +1][self.personaje_columna] ==1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] ==4:
            print("personaje,caja,espacio")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] =1  #se coloco la caja en el espacio
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] =0  #se coloco el personaje donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1#se actualizo la posicion del personaje

        #Moviento 8: [0,1,2] ->	[4,0,6]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila + 1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna ] == 2:
            print("personaje,caja,meta")
            self.mapa[self.personaje_fila +2][self.personaje_columna ] = 6 #se coloco la caja en la meta
            self.mapa[self.personaje_fila +1][self.personaje_columna ] = 0 #se coloca el personaje en el espacio
            self.mapa[self.personaje_fila +0][self.personaje_columna ] = 4 #se coloco el espacio en donde estaba el personaje
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
        #Moviemiento 9:  [0,6,4] -> [4,5,1] 
        if self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila +1][self.personaje_columna ] ==6 and self.mapa[self.personaje_fila + 2][self.personaje_columna ] == 4:
            print("Personaje, caja_meta, pasillo")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 1 #se coloco la caja en el pasillo
            self.mapa[self.personaje_fila +1][self.personaje_columna  ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila +0 ][self.personaje_columna ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
        #Movimiento 10:  [0,6,2] -> [4,5,6] 
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila +1][self.personaje_columna] ==6 and self.mapa[self.personaje_fila +2 ][self.personaje_columna ] ==2:
            print("Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila +2][self.personaje_columna  ] = 6 #se coloca la caja en la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 4 #donde estaba el personaje se coloco un espacio
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
        #Movimiento 11: [5,4] -> [2,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 4:
            print("Personaje_meta, pasillo")
            self.mapa[self.personaje_fila +1][self.personaje_columna ] = 0 #se coloca el personaje en el pasillo
            self.mapa[self.personaje_fila +0][self.personaje_columna ] = 2 #donde estabe personaje_meta se coloco una meta
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
        #Movimiento 12: [5,2] -> [2,5]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] ==2:
            print("Personaje_meta, meta")
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_fila+=1 #se actualiza la posicion del personaje
            
        #Movimiento 13: [5,1,4] -> [2,0,1]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila +1][self.personaje_columna ]== 1 and self.mapa[self.personaje_fila +2][self.personaje_columna ] == 4:
            print("Personaje_meta, caja, pasillo")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 1 #se coloca la caja en el espacio
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            
        #Movimiento 14: [5,1,2] -> [2,0,6]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila +2][self.personaje_columna ] ==2:
            print("Personaje_meta, caja, meta ")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 6 #se coloca la caja en donde esta la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
        #Movimiento 15 :[5,6,4] -> [2,5,1]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila +2][self.personaje_columna ] ==4:
            print("Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 1 #se coloca la caja en el pasillo
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
      
         #Movimiento 16 : [5,6,2] -> [2,5,6]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila +2][self.personaje_columna ] ==2:
            print("Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 6 #se coloca la caja_meta en el pasillo
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
            
            
            
            
    def arriba(self):
        
    
        # Movimiento 2: [4,0] -> [0,4]
        if self.mapa[self.personaje_fila -1][self.personaje_columna] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila -1][self.personaje_columna  ] = 0
            # Donde estaba el personaje pone el piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Actualiza la posicion del personaje
            self.personaje_columna-=1
                    
         
        #Movimiento 20 : [2,1,0] -> [6,0,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==2 and self.mapa[self.personaje_fila -1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila -2][self.personaje_columna] == 0:
            print("Personaje, caja y meta ")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 4 #se coloca piso donde estaba el personaje 
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 0 #se coloca personaje donde estaba la caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 6 # donde estaba la meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
        #Movimiento 21 : [4,6,0] -> [1,5,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==4 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila -2][self.personaje_columna ] == 0:
            print("Personaje, caja_meta y espacio ")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 4 #se coloca espacio donde estaba el personaje
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloca personaje meta donde estabacaja meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna] = 1 #donde estaba espacio se coloca caja
            self.personaje_columna -=1 #se actualiza la posicion del personaje
                        
            
        #Movimiento 22 : [2,6,0] -> [6,5,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==2 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila  -2][self.personaje_columna] == 0:
            print("Personaje, caja_meta y meta ")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 4 #se coloca espacio en donde estaba persona
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloca personaje meta en donde estaba caja meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 6 #donde estaba meta se coloca una caja meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
        
        
            #Movimiento 23 : [4,5] -> [0,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==4 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 5:
            print(" Personaje_meta y espacio ")
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 2 #se coloca meta donde estabapersonaje meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 0 #donde estaba espacio se coloca un personaje
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
                #Movimiento 24 : [2,5] -> [5,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==2 and self.mapa[self.personaje_fila  -1][self.personaje_columna] == 5:
            print(" Personaje_meta y meta ")
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 5 #donde estaba meta se coloca un personaje meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
                
        #Movimiento 25 : [4,1,5] -> [1,0,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] ==4 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila -2][self.personaje_columna ] == 5:
            print("Personaje_meta, caja y espacio ")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 0 #se coloca personaje en donde estaba caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 1 #donde estaba espacio se coloco la caja
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
        #Movimiento 26 : [2,1,5] -> [6,0,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila -2][self.personaje_columna ] == 5:
            print("Personaje_meta, caja y espacio ")
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0 #se coloca personaje donde estaba caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna] = 6 #donde estaba meta se caja meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
            
            #Movimiento 27 : [4,6,5] -> [1,5,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 4 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila -2][self.personaje_columna] == 5:
            print("Personaje_meta, caja y espacio ")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 2 #se coloca meta donde estaba personaje meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloca personaje meta donde estaba caja meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 1 #donde estaba espacio se coloca una caja
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            
            
                        #Movimiento 28 : [2,6,5] -> [6,5,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila -2][self.personaje_columna ] == 5:
            print("Personaje_meta, caja_meta y meta")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 2 #se coloca meta en donde estaba personaje meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloca personaje meta donde estaba caja meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 6 #donde estaba meta se coloco una cja
            self.personaje_columna -=1 #se actualiza la posicion del personajea
            
        
    def jugar(self):
        # Pide al usuario el nivel solo si no se ha seleccionado antes
        if not self.nivel_seleccionado:
            nivel = int(input("Selecciona el nivel (1, 2 o 3): "))
            self.seleccionar_nivel(nivel)
            self.imprimirMapa()

        while True:
            movimiento = input("Introduce W (arriba), A (izquierda), S (abajo), D (derecha) para mover al jugador:")
            if movimiento == 'd':
                self.derecha()
            elif movimiento == 'a':
                self.izquierda()
            elif movimiento == 'w':
                self.arriba()
            elif movimiento == 's':
                self.abajo()
            elif movimiento == 'exit':
                exit()

            # Imprime el mapa después de cada movimiento
            self.imprimirMapa()


# Inicia el juego
juego = Soko()
juego.jugar()
