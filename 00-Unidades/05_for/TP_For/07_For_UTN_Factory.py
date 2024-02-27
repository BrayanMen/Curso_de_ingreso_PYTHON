import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        postulantes = 10
        contador_nb = 0
        
        postulante_jr_menor = None
        bandera_int_jr = True
        
        nombre_postulante_jr_menor = None
        
        acc_edad_f = 0
        cont_sexo_f = 0
        acc_edad_m = 0
        cont_sexo_m = 0
        acc_edad_nb = 0
        cont_sexo_nb = 0
        
        cont_python = 0
        cont_js = 0
        cont_asp = 0
        
        for i in range(0, int(postulantes)):
            
            nombre = prompt("Ingresar","Ingresar nombre:")
            while nombre == '' or nombre == None:
                nombre = prompt("Error","Ingresar nombre valido:")
            
            while True: 
                edad = prompt("Ingresar","Ingresar edad valida:")
                edad = int(edad)
                if edad == None or int(edad) < 18:
                   print('Debe ser mayor de edad')
                else:
                    break
                
            puesto = prompt("Ingresar","Ingrese puesto (Jr - Ssr - Sr):").upper()
            while puesto != 'JR' and puesto != 'SSR' and puesto != 'SR':
                puesto = prompt("Error","Ingrese puesto (Jr - Ssr - Sr) valido:").upper()
            
            genero = prompt("Ingresar","Ingrese genero (F - M - NB):").upper()    
            while genero != 'F' and genero != 'M' and genero != 'NB':
                genero = prompt("Error","Ingrese genero (F - M - NB) valido:").upper()
                
            tecnología = prompt("Ingresar","Ingrese tecnologia (PYTHON - ASP.NET - JS):").upper()    
            while tecnología != 'PYTHON' and tecnología != 'ASP.NET' and tecnología != 'JS' : 
                tecnología = prompt("Error","Ingrese tecnologia (PYTHON - ASP.NET - JS) valido:").upper()
               
         #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
            if genero == 'NB' and (tecnología == 'JS' or tecnología == 'ASP.NET'):
                if int(edad) > 24 and int(edad) < 40 and puesto == 'SSR':
                    contador_nb += 1
                    
        #b. Nombre del postulante Jr con menor edad.
            if puesto == 'JR':
                if bandera_int_jr:
                    bandera_int_jr = False
                    postulante_jr_menor = int(edad)
                    nombre_postulante_jr_menor = nombre
                else:
                    if edad < postulante_jr_menor:
                        postulante_jr_menor = int(edad)
                        nombre_postulante_jr_menor = nombre     
                
        #c. Promedio de edades por género.
            if genero == 'F':
                acc_edad_f += edad
                cont_sexo_f += 1
            else:
                if genero == 'M':
                    acc_edad_m += edad
                    cont_sexo_m += 1
                else:
                    acc_edad_nb += edad
                    cont_sexo_nb += 1
                    
            if cont_sexo_f > 0:      
                promedio_genero_f = acc_edad_f / cont_sexo_f
            else:
                promedio_genero_f = 'No hay postulantes F'
                
            if cont_sexo_m > 0:      
                promedio_genero_m = acc_edad_m / cont_sexo_m
            else:
                promedio_genero_m = 'No hay postulantes M'
            
            if cont_sexo_nb > 0:      
                promedio_genero_nb = acc_edad_nb / cont_sexo_nb
            else:
                promedio_genero_nb = 'No hay postulantes NB'
                
        #d. Tecnologia con mas postulantes (solo hay una).
            if tecnología == 'JS':
                cont_js += 1
            else:
                if tecnología == 'PYTHON':
                    cont_python += 1
                else:
                    cont_asp += 1
                    
            if cont_asp > cont_js and cont_asp > cont_python:
                msj_tech = 'ASP.NET'
            else:
                if cont_python > cont_js:
                    msj_tech =  'PYTHON'
                else:
                    msj_tech = 'JS'
                    
        #e. Porcentaje de postulantes de cada genero.
        
            promedio_post_f = (cont_sexo_f / postulantes) * 100
            promedio_post_m = (cont_sexo_m / postulantes) * 100
            promedio_post_nb = (cont_sexo_nb / postulantes)  * 100
            
                
        print(f'Cantidad de géneros NB para el puesto SSR: {contador_nb}')
        print(f'Nombre del postulante Jr más joven: {nombre_postulante_jr_menor} con {postulante_jr_menor} años.')
        print(f'Promedio F: {promedio_genero_f}\nPromedio M: {promedio_genero_m}\nPromedio NB: {promedio_genero_nb}')
        print(f'La tecnologia con mas usuariohs es: {msj_tech}')
        print(f'Promedio postulaciones F: {promedio_post_f}\nPromedio postulaciones M: {promedio_post_m}\nPromedio postulaciones NB: {promedio_post_nb}')

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
