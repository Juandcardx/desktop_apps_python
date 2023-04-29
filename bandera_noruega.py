# crear bandera de noruega
from tkinter import*

ventana_principal = Tk() # ALMACENA UN OBJETOO DE TIPO TK()

# titulo de la ventana
ventana_principal.title()

# Tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventama
ventana_principal.config(bg="white")

# ----------------------------------
# frame input data
# ----------------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=140, height=230)
frame_entrada.place(x=0, y=0)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="dark blue", width=230, height=230)
frame_entrada.place(x=230, y=0)
# run 
# se ejecuta la funcion (metodo) mainloop() de la clase TK() atravez de la instancia ventana_principal. 
# Este metodo despleja una ventana simple  en pantalla y queda a la espera de lo que el usuario haga. 
# Cada accion del ussuario se conoce como evento. El mainloop() en un bucle infinito

ventana_principal.mainloop()  # tamaño, titulo, cuadros de texto, widgets...