# plataforma_estudiantes
programa usando tkinter para hacer una plataforma de estudiantes

para la actitudinal dnde estan las notas
   # etiqueta para el texto
lb_texto = Label(toplevel_notas, text = "Ingrese sus notas")
lb_texto.config(bg="orange2", fg="black", font=("italik", 30))
lb_texto.place(x=150, y=15)

    # etiqueta para actitudinal
lb_nombre = Label(frame_blanco, text = "Nombre del estudiante = ")
lb_nombre.config(bg="white", fg="orange2", font=("Helvetica", 18))
lb_nombre.place(x=30, y=155)