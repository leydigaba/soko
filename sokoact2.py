class Soko:

    def __init__(self):
        self.mapa = None
        self.nivel_seleccionado = False
        self.personaje_columna = None
        self.personaje_fila = None 
        self.nivel_actual = None  # Para llevar registro del nivel actual
        
    def seleccionar_nivel(self, nivel):
        
        if nivel == 1:
            # Define el mapa del nivel 1
            self.mapa = [
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 4, 0, 1, 2, 4, 4, 4, 3],
                [3, 4, 1, 4, 2, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 4, 4, 4, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3]
            ]
            self.personaje_columna = 2
            self.personaje_fila = 1
            self.nivel_seleccionado = True
            self.nivel_actual = 1
            
        elif nivel == 2:
            # Define el mapa del nivel 2
            
            self.mapa = [
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 4, 0, 1, 2, 4, 1, 2, 3],
                [3, 4, 4, 4, 4, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 4, 4, 4, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3]
            ]
            self.personaje_columna = 2
            self.personaje_fila = 1
            self.nivel_seleccionado = True
            self.nivel_actual = 1
            
            pass

        else:
            print("Nivel incorrecto. Cerrando el juego.")
            exit()

        # Establece el indicador de nivel seleccionado en Verdadero
        self.nivel_seleccionado = True
        return True
            
    def imprimirMapa(self):
            if self.mapa is None:
                print("Mapa no seleccionado.")
                return
            
            simbolos = {
                0: '🐇',  # Personaje
                1: '⬛​​',  # Caja
                2: '🥕',  # Meta
                3: '⚪​',   # Pared
                4: '​🟩',   # Suelo
                5: '🐰',  # Personaje en meta
                6: '✅'   # Caja en meta
            }
           
           
           
  
            for fila in self.mapa:
            # Mapea cada número a su símbolo correspondiente y luego imprime la fila
               print(''.join(simbolos[num] for num in fila))


    def limpiar_pantalla(self):
        # Esta función simula limpiar la pantalla imprimiendo varias líneas en blanco
        print('\n' * 8)
        
        
        
    def jugar(self):
        # Pide al usuario el nivel solo si no se ha seleccionado antes
        if not self.nivel_seleccionado:
            nivel = int(input("Selecciona el nivel (1 o 2 ): "))
            print("Estás jugando el nivel " + str(nivel))
            self.seleccionar_nivel(nivel)
            self.imprimirMapa()
    

        while True:
            movimiento = input("Introduce W (arriba), A (izquierda), S (abajo), D (derecha) para mover al jugador:")
            if movimiento == 'd':
                self.derecha()
            elif movimiento == 'a':
                self.izquierda()
                print("se mueve")
            elif movimiento == 'w':
                self.arriba()
            elif movimiento == 's':
                self.abajo()
            elif movimiento == 'exit':
                exit()
            elif movimiento == 'r':
                print("Reiniciando nivel...")
                self.seleccionar_nivel(self.nivel_actual)  # Reiniciar el nivel actual
                self.imprimirMapa()
            elif movimiento == 'exit':
                continue  # Continuar con el bucle sin imprimir el mapa nuevamente después del reinicio
            

        
        
        
            if self.nivel_terminado():
                print("¡Felicidades! Has completado el nivel.")
                self.imprimirMapa()
                continuar = input("¿Quieres seguir jugando? (si/no): ")
                if continuar.lower() != 'si':
                    print("¡Hasta luego!")
                    exit()
                    
                else:
                    # Reiniciar variables para el siguiente nivel
                    self.nivel_seleccionado = False
                    self.personaje_columna = None
                    self.personaje_fila = None
                    
                    nivel = 2  # Cambia esto al nivel que deseas cargar 
                    self.seleccionar_nivel(nivel)
                    print("Estás jugando el nivel " + str(nivel))
                    self.imprimirMapa()
                    #self.seleccionar_nivel(nivel)
                    #self.imprimirMapa()
            else:
                # Imprime el mapa después de cada movimiento
                self.imprimirMapa()

    def nivel_terminado(self):
        for fila in self.mapa:
            for elemento in fila:
                if elemento == 1:  # Si hay una caja en el mapa
                    return False
        return True  # Si no hay cajas en el mapa, el nivel está terminado
    



    def derecha(self):
        # Movimiento 5: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            print("Movimiento realizado:personaje,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna +1 ] = 0 #se coloca el personaje en la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna +=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio, personaje")

        #Moviento 6: [0,2]  ->	[4,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            print("Movimiento realizado:personaje,meta")
            self.mapa[self.personaje_fila][self.personaje_columna +1] =5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna +0] =4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna +=1 #se acualizo la posicion del personaje
            print("Posición actual: espacio, personaje_meta")
            
            
       #Movimiento 7: [0,1,4]  ->	[4,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna+1] ==1 and self.mapa[self.personaje_fila][self.personaje_columna+2] ==4:
            print("Movimiento realizado: personaje,caja,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] =1  #se coloco la caja en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna + 1] =0  #se coloco el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna +=1#se actualizo la posicion del personaje
            print("Posición actual: espacio,personaje,caja")
            

        #Moviento 8: [0,1,2] ->	[4,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            print("Movimiento realizado: personaje,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 6 #se coloco la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 0 #se coloca el personaje en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna +0] = 4 #se coloco el espacio en donde estaba el personaje
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,personaje,caja_meta")
            
        #Moviemiento 9:  [0,6,4] -> [4,5,1] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna +1] ==6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            print("Movimiento ralizado:Personaje, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 #se coloco la caja en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna +1 ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna +0 ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,caja")
            
        #Movimiento 10:  [0,6,2] -> [4,5,6] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna +1] ==6 and self.mapa[self.personaje_fila ][self.personaje_columna +2] ==2:
            print(" Movimiento ralizado: Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna +2 ] = 6 #se coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 4 #donde estaba el personaje se coloco un espacio
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,Caja_meta")
            
            
        #Movimiento 11: [5,4] -> [2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 4:
            print("Movimiento realizado:Personaje_meta,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 0 #se coloca el personaje en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna +0] = 2 #donde estabe personaje_meta se coloco una meta
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,personaje")
            
        #Movimiento 12: [5,2] -> [2,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna +1] ==2:
            print("Movimiento realizado: Personaje_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje_meta")
            
        #Movimiento 13: [5,1,4] -> [2,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna +1]== 1 and self.mapa[self.personaje_fila][self.personaje_columna +2] == 4:
            print("Movimiento realizado:Personaje_meta, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 #se coloca la caja en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_columna+=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje,caja")
            
        #Movimiento 14: [5,1,2] -> [2,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna +2] ==2:
            print("Movimiento realizado: Personaje_meta, caja, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 #se coloca la caja en donde esta la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna +=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje, caja_meta")
            
        #Movimiento 15 :[5,6,4] -> [2,5,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna +2] ==4:
            print("Movimiento realizado:Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 #se coloca la caja en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna +=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje_meta,caja")

         #Movimiento 16 : [5,6,2] -> [2,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna +1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna +2] ==2:
            print("Movimiento realizado:Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 #se coloca la caja_meta en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna +=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje_meta,caja_meta")
        
            
       
            
    def izquierda(self):
        # Movimiento 5: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            print("Movimiento realizado: personaje,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna -1 ] = 0 #se coloca el personaje en la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio, personaje")
            

        #Moviento 6: [0,2]  ->	[4,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
            print("Movimiento realizado:personaje,meta")
            self.mapa[self.personaje_fila][self.personaje_columna -1] =5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna -0] =4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna -=1 #se acualizo la posicion del personaje
            print("Posición actual: espacio, personaje_meta")
            
       #Movimiento 7: [0,1,4]  ->	[4,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna-1] ==1 and self.mapa[self.personaje_fila][self.personaje_columna -2] ==4:
            print("Movimiento realizado: personaje,caja,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] =1  #se coloco la caja en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna - 1] =0  #se coloco el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna -=1#se actualizo la posicion del personaje
            print("Posición actual: espacio,personaje,caja")

        #Moviento 8: [0,1,2] ->	[4,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            print("Movimiento realizado: personaje,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 6 #se coloco la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 0 #se coloca el personaje en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna -0] = 4 #se coloco el espacio en donde estaba el personaje
            self.personaje_columna-=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,personaje,caja_meta")
            
        #Moviemiento 9:  [0,6,4] -> [4,5,1] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila][self.personaje_columna -1] ==6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            print("Movimiento realizado:Personaje, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1 #se coloco la caja en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0 ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,caja")
            
        #Movimiento 10:  [0,6,2] -> [4,5,6] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] ==6 and self.mapa[self.personaje_fila ][self.personaje_columna - 2] ==2:
            print(" Movimiento ralizado: Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 6 #se coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 4 #donde estaba el personaje se coloco un espacio
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,Caja_meta")
            
        #Movimiento 11: [5,4] -> [2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 4:
            print("Movimiento realizado:Personaje_meta,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0 #se coloca el personaje en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 2 #donde estabe personaje_meta se coloco una meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,personaje") 
            
        #Movimiento 12: [5,2] -> [2,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] ==2:
            print("Movimiento realizado: Personaje_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje_meta")
            
        #Movimiento 13: [5,1,4] -> [2,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna -1]== 1 and self.mapa[self.personaje_fila][self.personaje_columna -2] == 4:
            print("Movimiento realizado:Personaje_meta, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1 #se coloca la caja en el espacio
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje,caja")
            
        #Movimiento 14: [5,1,2] -> [2,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna -2] ==2:
            print("Movimiento realizado: Personaje_meta, caja, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6 #se coloca la caja en donde esta la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje, caja_meta")
            
        #Movimiento 15 :[5,6,4] -> [2,5,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna -2] ==4:
            print("Movimiento realizado:Personaje_meta, caja_meta, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1 #se coloca la caja en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje_meta,caja")
            
        #Movimiento 16:
        
         #Movimiento 15 : [5,6,2] -> [2,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila][self.personaje_columna -1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna -2] ==2:
            print("Movimiento realizado:Personaje_meta, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6 #se coloca la caja_meta en el pasillo
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 0] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_columna -=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje_meta,caja_meta")
            
            
                
            
    def arriba(self):
        
        
        # Movimiento 29: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila  - 1][self.personaje_columna] == 4:
            print("Movimiento realizado: personaje,espacio")
            self.mapa[self.personaje_fila -1][self.personaje_columna ] = 0 #se coloca el personaje en la caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila -=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio, personaje")
            

        #Moviento 30: [0,2]  ->	[4,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            print("Movimiento realizado:personaje,meta")
            self.mapa[self.personaje_fila -1][self.personaje_columna ] =5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila -0][self.personaje_columna ] =4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila -=1 #se acualizo la posicion del personaje
            print("Posición actual: espacio, personaje_meta")
            

        #Movimiento 31: [0,1,4]  ->	[4,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila -1][self.personaje_columna] ==1 and self.mapa[self.personaje_fila -2][self.personaje_columna] ==4:
            print("Movimiento realizado: personaje,caja,espacio")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] =1  #se coloco la caja en el espacio
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] =0  #se coloco el personaje donde estaba la caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] =4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila -=1#se actualizo la posicion del personaje
            print("Posición actual: espacio,personaje,caja")

        #Moviento 32: [0,1,2] ->	[4,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila - 1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna ] == 2:
            print("Movimiento realizado: personaje,caja,meta")
            self.mapa[self.personaje_fila -2][self.personaje_columna ] = 6 #se coloco la caja en la meta
            self.mapa[self.personaje_fila -1][self.personaje_columna ] = 0 #se coloca el personaje en el espacio
            self.mapa[self.personaje_fila -0][self.personaje_columna ] = 4 #se coloco el espacio en donde estaba el personaje
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,personaje,caja_meta")
            
            
        #Moviemiento 33:  [0,6,4] -> [4,5,1] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila  -1][self.personaje_columna ] ==6 and self.mapa[self.personaje_fila - 2][self.personaje_columna ] == 4:
            print("Movimiento realizado:Personaje, caja_meta, espacio")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 1 #se coloco la caja en el pasillo
            self.mapa[self.personaje_fila -1][self.personaje_columna  ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila -0 ][self.personaje_columna ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,caja")
            
            
        #Movimiento 34:  [0,6,2] -> [4,5,6] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila -1][self.personaje_columna] ==6 and self.mapa[self.personaje_fila -2][self.personaje_columna ] ==2:
            print(" Movimiento realizado: Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila -2][self.personaje_columna  ] = 6 #se coloca la caja en la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 4 #donde estaba el personaje se coloco un espacio
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,Caja_meta")
            
            
        #Movimiento 35: [5,4] -> [2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 4:
            print("Movimiento realizado:Personaje_meta,espacio")
            self.mapa[self.personaje_fila -1][self.personaje_columna ] = 0 #se coloca el personaje en el pasillo
            self.mapa[self.personaje_fila -0][self.personaje_columna ] = 2 #donde estabe personaje_meta se coloco una meta
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,personaje") 
            
            
        #Movimiento 36: [5,2] -> [2,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila -1][self.personaje_columna ] ==2:
            print("Movimiento realizado: Personaje_meta, meta")
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje_meta") 
            
        #Movimiento 37: [5,1,4] -> [2,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila -1][self.personaje_columna ]== 1 and self.mapa[self.personaje_fila -2][self.personaje_columna ] == 4:
            print("Movimiento realizado:Personaje_meta, caja, pasillo")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 1 #se coloca la caja en el espacio
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje,caja")
            
        #Movimiento 38: [5,1,2] -> [2,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila -2][self.personaje_columna ] ==2:
            print("Movimiento realizado:Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila -2][self.personaje_columna ] = 6 #se coloca la caja en donde esta la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila -=1 #se actualiza la posicion del personaje
            
        #Movimiento 39 :[5,6,4] -> [2,5,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila -2][self.personaje_columna ] ==4:
            print("MoPersonaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 1 #se coloca la caja en el pasillo
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila -=1 #se actualiza la posicion del personaje
            print("Movimiento realizado: movimiento actual:meta, pesonaje, caja_meta")
            
  
        
         #Movimiento 40 : [5,6,2] -> [2,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila -1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila -2][self.personaje_columna ] ==2:
            print("Movimiento realizado:Personaje_meta, caja_meta, meta")
            self.mapa[self.personaje_fila - 2][self.personaje_columna ] = 6 #se coloca la caja_meta en el pasillo
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila - 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila -=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje_meta,caja_meta")
            
            
            
            
            
            
    def abajo(self):
        
        
        # Movimiento 41: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna ] == 4:
            print("Movimiento realizado: personaje,espacio")
            self.mapa[self.personaje_fila +1][self.personaje_columna] = 0 #se coloca el personaje en la caja
            self.mapa[self.personaje_fila +0][self.personaje_columna] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio, personaje")

        #Moviento 42:  [4,0] -> [0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna ] == 2:
            print("Movimiento realizado:personaje,meta")
            self.mapa[self.personaje_fila +1][self.personaje_columna] =5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila +0][self.personaje_columna ] =4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1 #se acualizo la posicion del personaje
            print("Posición actual: espacio, personaje_meta")

        #Movimiento 43: [0,1,4]  ->	[4,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila +1][self.personaje_columna] ==1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] ==4:
            print("Movimiento realizado: personaje,caja,espacio")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] =1  #se coloco la caja en el espacio
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] =0  #se coloco el personaje donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1#se actualizo la posicion del personaje
            print("Posición actual: espacio,personaje,caja")

        #Moviento 44: [0,1,2] ->	[4,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila + 1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna ] == 2:
            print("Movimiento realizado: personaje,caja,meta")
            self.mapa[self.personaje_fila +2][self.personaje_columna ] = 6 #se coloco la caja en la meta
            self.mapa[self.personaje_fila +1][self.personaje_columna ] = 0 #se coloca el personaje en el espacio
            self.mapa[self.personaje_fila +0][self.personaje_columna ] = 4 #se coloco el espacio en donde estaba el personaje
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,personaje,caja_meta")
            
        #Moviemiento 45:  [0,6,4] -> [4,5,1] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==0 and self.mapa[self.personaje_fila +1][self.personaje_columna ] ==6 and self.mapa[self.personaje_fila + 2][self.personaje_columna ] == 4:
            print("Movimiento realizado:Personaje, caja_meta, espacio")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 1 #se coloco la caja en el pasillo
            self.mapa[self.personaje_fila +1][self.personaje_columna  ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila +0 ][self.personaje_columna ] = 4 #se coloco el espacio donde estaba el personaje
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,caja")
            
            
        #Movimiento 46:  [0,6,2] -> [4,5,6] 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila +1][self.personaje_columna] ==6 and self.mapa[self.personaje_fila +2 ][self.personaje_columna ] ==2:
            print(" Movimiento realizado: Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila +2][self.personaje_columna  ] = 6 #se coloca la caja en la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloco el personaje en la meta
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 4 #donde estaba el personaje se coloco un espacio
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            print("Posición actual: espacio,pesonaje_meta,Caja_meta")
            
            
        #Movimiento 47: [5,4] -> [2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 4:
            print("Movimiento realizado:Personaje_meta,espacio")
            self.mapa[self.personaje_fila +1][self.personaje_columna ] = 0 #se coloca el personaje en el pasillo
            self.mapa[self.personaje_fila +0][self.personaje_columna ] = 2 #donde estabe personaje_meta se coloco una meta
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,personaje") 
            
            
        #Movimiento 48: [5,2] -> [2,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] ==2:
            print("Movimiento realizado: Personaje_meta, meta")
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_fila+=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje_meta") 
            
            
        #Movimiento 49: [5,1,4] -> [2,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila +1][self.personaje_columna ]== 1 and self.mapa[self.personaje_fila +2][self.personaje_columna ] == 4:
            print("Movimiento realizado:Personaje_meta, caja, pasillo")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 1 #se coloca la caja en el espacio
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloco la meta
            self.personaje_fila-=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta,pesonaje,caja")
            
            
        #Movimiento 50: [5,1,2] -> [2,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 1 and self.mapa[self.personaje_fila +2][self.personaje_columna ] ==2:
            print("Movimiento realizado: Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 6 #se coloca la caja en donde esta la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 0 #se coloca el personaje en donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            print("Movimiento actual:meta, pesonaje, caja_meta")
            
            
        #Movimiento 51:[5,6,4] -> [2,5,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila +2][self.personaje_columna ] ==4:
            print("Personaje_meta, caja_meta, pasillo ")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 1 #se coloca la caja en el pasillo
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila +=1 #se actualiza la posicion del personaje
            
      
         #Movimiento 52: [5,6,2] -> [2,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] ==5 and self.mapa[self.personaje_fila +1][self.personaje_columna ] == 6 and self.mapa[self.personaje_fila +2][self.personaje_columna ] ==2:
            print("Movimiento realizado:Personaje_meta, caja_meta, meta")
            self.mapa[self.personaje_fila + 2][self.personaje_columna ] = 6 #se coloca la caja_meta en el pasillo
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5 #se coloca el personaje en la meta donde estaba la caja
            self.mapa[self.personaje_fila + 0][self.personaje_columna ] = 2 #donde estaba el personaje se coloca  la meta
            self.personaje_fila +=1 #se actualiza la posicion del 
            print("Movimiento actual:meta, pesonaje_meta,caja_meta")
            
            
            
   
            
            

            
            
    

    
    
   
# Inicia el juego
juego = Soko()
juego.jugar()

