
#------------------------------
# David Fernando Rangel Fonseca
#------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#------------------------------
# funciones de la app
#------------------------------

# abrir toplevel centigrados
def abrir_toplevel_notas():
    global toplevel_notas
    toplevel_notas = Toplevel()
    toplevel_notas.title("Notas")
    toplevel_notas.resizable(False, False)
    toplevel_notas.geometry("600x500")
    toplevel_notas.config(bg="orange2")

   # etiqueta para el texto 
    lb_texto = Label(toplevel_notas, text = "Ingrese sus notas")
    lb_texto.config(bg="orange2", fg="black", font=("italik", 30))
    lb_texto.place(x=150, y=15)

    



# borrar
def borrar():
    messagebox.showinfo("David Fernando Rangel Fonseca","Los datos serán borrados")

# salir
def salir():
    messagebox.showinfo("David Fernando Rangel Fonseca", "La app se va a cerrar")
    ventana_principal.destroy()

#------------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("David Fernando Rangel Fonseca")

# tamaño de la ventana
ventana_principal.geometry("600x500")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------
# frame entrada
#------------------------------
frame_entrada= Frame(ventana_principal)
frame_entrada.config(bg="orange2", width=600, height=500)
frame_entrada.place(x=0, y=0)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=580, height=480)
frame_blanco.place(x=10, y=10)

#------------------------------
# frame naranja
#------------------------------
frame_orange= Frame(ventana_principal)
frame_orange.config(bg="orange2", width=600, height=125)
frame_orange.place(x=0, y=10)

#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_separator()
menu_convertir.add_command(label="Borrar", command=borrar)

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Menú", menu=menu_convertir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

# imagen para la app
logo = PhotoImage(file="img/integra.png")
lb_logo = Label(frame_orange, image=logo, bg="orange2")
lb_logo.place(x=50,y=-5)


# titulo de la app
titulo = Label(frame_orange, text="Rangelitos")
titulo.config(bg = "orange2",fg="black", font=("Helvetica", 40))
titulo.place(x=315,y=20)

# etiqueta para el nombre
lb_nombre = Label(frame_blanco, text = "Nombre del estudiante = ")
lb_nombre.config(bg="white", fg="orange2", font=("Helvetica", 18))
lb_nombre.place(x=30, y=155)

# caja de texto para el nombre
entry_nombre = Entry(frame_blanco, textvariable=lb_nombre)
entry_nombre.config(bg="white", fg="orange2", font=("Times New Roman", 18), width=20)
entry_nombre.focus_set()
entry_nombre.place(x=300, y=150)

# etiqueta para el número telefónico
lb_telefono = Label(frame_blanco, text = "Número de Teléfono = ")
lb_telefono.config(bg="white", fg="orange2", font=("Helvetica", 18))
lb_telefono.place(x=30, y=215)

# caja de texto para el número telefónico
entry_telefono = Entry(frame_blanco, textvariable=lb_telefono)
entry_telefono.config(bg="white", fg="orange2", font=("Times New Roman", 18), width=20)
entry_telefono.focus_set()
entry_telefono.place(x=300, y=210)

# etiqueta para el correo
lb_correo = Label(frame_blanco, text = "Correo Electrónico = ")
lb_correo.config(bg="white", fg="orange2", font=("Helvetica", 18))
lb_correo.place(x=30, y=275)

# caja de texto para el correo
entry_correo = Entry(frame_blanco, textvariable=lb_correo)
entry_correo.config(bg="white", fg="orange2", font=("Times New Roman", 18), width=20)
entry_correo.focus_set()
entry_correo.place(x=300, y=270)

# boton calcular 
bt_convertir = Button(frame_blanco,text="siguiente ", command=abrir_toplevel_notas)
bt_convertir.place(x=230, y=360, width=100, height=30)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()