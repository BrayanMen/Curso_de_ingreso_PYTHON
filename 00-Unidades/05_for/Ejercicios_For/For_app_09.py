import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre:
apellido:
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_secreto = random.randint(1, 100)
        print(numero_secreto)
        
        for intentos in range(1, 10):
            numero = prompt('Ingresar', 'Ingresar numero:')
            numero = int(numero)
            if numero_secreto == int(numero):
                #1° intento: “Usted es un psíquico”.
                if intentos == 1:
                    print('“Usted es un psíquico”.')
                else:
	            #2° intento: “Excelente percepción”.
                    if intentos == 2:
                        print('“Excelente percepción”.')
                    else:
	            #3° intento: “Esto es suerte”.
                        if intentos == 3:
                            print('“Esto es suerte”.')
                        else:
	            #4° hasta 6° intento: “Excelente técnica”.
                            if intentos < 3 or intentos > 6:
                                print('“Excelente técnica”.')
                            else:
                                if intentos == 7:
	            #7 intentos: “Perdiste, suerte para la próxima”
                                    print('“Perdiste, suerte para la próxima”.')
                                else:
                                    print('Fracaso rotundo!')
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()