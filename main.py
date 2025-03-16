from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]
 
operador = ''
#------------------------------Funciones-------------------------------------------------------
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)
def click_borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)
#Resultado

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def recibo():
    texto_recibo.delete(1.0, END)  # Limpia el contenido actual del recibo
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day} / {fecha.month} / {fecha.year} - {fecha.hour}:{fecha.minute}'

    # Información inicial del recibo
    texto_recibo.insert(END, f'Datos:\t {num_recibo} \t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\t Cant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    # Insertar comidas seleccionadas en el recibo
    for index, var in enumerate(variables_comida):
        if var.get() == 1:  # Si el Checkbutton está marcado
            cantidad = int(texto_comida[index].get())
            precio_unitario = precios_comida[index]
            costo_comida = cantidad * precio_unitario
            texto_recibo.insert(END, f'{lista_comidas[index]}\t\t{cantidad}\t${costo_comida:.2f}\n')

    # Insertar bebidas seleccionadas en el recibo
    for index, var in enumerate(variables_bebida):
        if var.get() == 1:
            cantidad = int(texto_bebidas[index].get())
            precio_unitario = precios_bebida[index]
            costo_bebida = cantidad * precio_unitario
            texto_recibo.insert(END, f'{lista_bebidas[index]}\t\t{cantidad}\t${costo_bebida:.2f}\n')

    # Insertar postres seleccionados en el recibo
    for index, var in enumerate(variables_postre):
        if var.get() == 1:
            cantidad = int(texto_postres[index].get())
            precio_unitario = precios_postres[index]
            costo_postre = cantidad * precio_unitario
            texto_recibo.insert(END, f'{lista_postres[index]}\t\t{cantidad}\t${costo_postre:.2f}\n')

    # Líneas finales del recibo
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Subtotal-Comidas:\t\t\t${var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Subtotal-Bebidas:\t\t\t${var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Subtotal-Postres:\t\t\t${var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    
    texto_recibo.insert(END, f'Subtotal:\t\t\t${var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos:\t\t\t${var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t\t${var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, f'\t\t Gracias por su Visita')


def guardar_recibo():
    contenido_recibo = texto_recibo.get(1.0, END)  # Obtén el contenido del widget de texto
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='txt')
    archivo.write(contenido_recibo)  # Escribe el contenido en el archivo
    archivo.close()
    messagebox.showinfo('Su recibo fue Guardado')  # Mensaje de confirmación en consola
 


def calcular_total():
    costo_comida = 0
    costo_bebida = 0
    costo_postre = 0
    precioFinal = 0
    impuesto = 0.07
    # Calcula el total para comidas
    for index, var in enumerate(variables_comida):
        if var.get() == 1:  # Si el Checkbutton está activado
            cantidad = int(texto_comida[index].get())#Obtiene la cantidad ingresada en el cuadro de texto (Entry) asociado a esa comida.
            precio_unitario = precios_comida[index]#Obtiene el precio unitario de la lista precios_comida usando el mismo índice.
            costo_comida += cantidad * precio_unitario#Calcula el subtotal multiplicando la cantidad seleccionada por el precio unitario
            
    # Calcula el total para bebidas
    for index, var in enumerate(variables_bebida):
        if var.get() == 1:
            cantidad = int(texto_bebidas[index].get())
            precio_unitario = precios_bebida[index]
            costo_bebida += cantidad * precio_unitario

    # Calcula el total para postres
    for index, var in enumerate(variables_postre):
        if var.get() == 1:
            cantidad = int(texto_postres[index].get())
            precio_unitario = precios_postres[index]
            costo_postre += cantidad * precio_unitario
         
                  
    subtotales = costo_comida + costo_bebida + costo_postre
    impuestos = subtotales * impuesto
    precioFinal = subtotales + impuestos

    var_costo_comida.set(f'$ {round(costo_comida, 2 )}')
    var_costo_bebida.set(f'$ {round(costo_bebida, 2 )}')
    var_costo_postre.set(f'$ {round(costo_postre, 2 )}')
    var_subtotal.set(f'${round (subtotales,2)}')
    var_impuesto.set(f'$ {round(impuestos,2)}')
    var_total.set(f'${round(precioFinal,2)}')

#LLegamos al final receteamos toda la pantalla 
def recetear_all():

    # Limpia el contenido del recibo
    texto_recibo.delete(1.0, END)

    # Reinicia las variables numéricas
    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")
    
    # Limpia las entradas de texto (Entry)
    for entrada in texto_comida:
            entrada.set('0')
    for entrada in texto_bebidas:
            entrada.set('0')
    for entrada in texto_postres:
            entrada.set('0')
    
    # Eliminamos elvalor de la ventanao cantidad
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)  
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
    #Desmarca los Checkbuttons

    for var in variables_comida:
        var.set(0)
    for var in variables_bebida:
        var.set(0)
    for var in variables_postre:
        var.set(0)

#------------------------------ End Funciones-------------------------------------------------------    
def revisar_check_comida():
    for index, var in enumerate(variables_comida):
        if var.get() == 1:  # Si el Checkbutton está activado
            cuadros_comida[index].config(state='normal')
        else:  # Si está desactivado
            cuadros_comida[index].config(state='disabled')
            texto_comida[index].set('0')
def revisar_check_bebida():
    for index, var in enumerate(variables_bebida):
        if var.get() == 1:  # Si el Checkbutton está activado
            cuadros_bebidas[index].config(state='normal')
        else:  # Si está desactivado
            cuadros_bebidas[index].config(state='disabled')
            texto_bebidas[index].set('0')
def revisar_check_postre():
    for index, var in enumerate(variables_postre):
        if var.get() == 1:  # Si el Checkbutton está activado
            cuadros_postres[index].config(state='normal')
        else:  # Si está desactivado
            
            cuadros_postres[index].config(state='disabled')
            texto_postres[index].set('0')

# Iniciamos la aplicacion tk inter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')#Ancho y alto 


#Evitar Maximizar
#aplicacion.resizable(0,0) # Esto lo que hace es evitar que el usuario agrande o maximise la pantalla
# title
aplicacion.title("Restaurand-Sistema de facturacion")
# Color de fondo pantalla
aplicacion.config(bg='lightyellow')

# Cuadrante superior-----------------Panel1------------------------------------------------------------------------
panel_superior = Frame(aplicacion,bd=1 , relief='flat')#opciones de relieve FLAT, RAISED ,SUNKEN,GROOVE,RIDGE
panel_superior.pack(side=TOP)# Lo ubicamos arriba
#Titulo panel superior
etiqueta_titulo = Label(panel_superior,text='Sistema de facturacion', fg='gray',
                        font=('Dosis' ,40,), bg="lightyellow",width=27)
etiqueta_titulo.grid(row=0 , column=0)

# Cuadrante superior-----------------Panel1 Fin------------------------------------------------------------------------



#Cuadrante izquierdo ----------------Panel2-------------------------------------------------------------------------
panel_izquierdo = Frame(aplicacion,bd=1 , relief='flat')
panel_izquierdo.pack(side=LEFT) #Lo ubicamos a la izquierda

#Panel de costos
panel_costos = Frame(panel_izquierdo, bd=1 , relief=FLAT, bg='gray' )
panel_costos.pack(side=BOTTOM)# Lo ubicamos abajo de todo

#Panel menu
panel_comida = LabelFrame(panel_izquierdo,bd=1,relief=FLAT,text='Comida',font=('Dosis',19,'bold'),fg='azure4' )
panel_comida.pack(side=LEFT)# Lo ubicamos a la izquierda


#Panel de bebidas
panel_bebida = LabelFrame(panel_izquierdo,bd=1,relief=FLAT,text='Bebidas',font=('Dosis',19,'bold'),fg='azure4' )
panel_bebida.pack(side=LEFT)# Lo ubicamos a la izqyuierda

#Panel de postres
panel_postres = LabelFrame(panel_izquierdo,bd=1,relief=FLAT,text='Postres',font=('Dosis',19,'bold'),fg='azure4' )
panel_postres.pack()# Lo ubicamos a la izqyuierda
#Cuadrante izquierdo-----------------Panel2 Fin----------------------------------------------------------------------------



#Cuadrante Derecho---------------------------------Panel3----------------------------------------------------------------------
panel_derecho = Frame(aplicacion,bd=1,relief='flat')
panel_derecho.pack(side=RIGHT) #Lo ubicamos a la derecha

#Panel Calculadora
panel_calculadora = Frame(panel_derecho,bd=1,relief=FLAT,bg='gray')
panel_calculadora.pack(side=TOP)#SI no escribis nada por defecto se ubica arriba Top

#Panel recibo
panel_recibo = Frame(panel_derecho,bd=1,relief=FLAT,bg='gray')
panel_recibo.pack()#Si no escribis nada por defecto sae ubica abajo del top


#Panel de botones
panel_botones = Frame(panel_derecho,bd=1,relief=FLAT,bg='gray')
panel_botones.pack()

#Cuadrante Derecho-----------------Panel3 Fin------------------------------------------------------------------------

#lista de comidas 

lista_comidas = ['pollo', 'cordero', 'estofado', 'arroz amarillo' , 'guiso de lentejas','costeletas con pure', 'canelones ', 'pescado']
lista_bebidas =  ['gaseosas' , 'vinos','sodas','cervezas','agua','jugo Frutales','cafe', 'Te']
lista_postres = ['helados','fruta','flan','mouse','brownies','facturas','Lemon pie','Torta de chocolate']



# Generamos items comida 
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

# Generamos items bebidas 
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0

# Generamos items postres 
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0

import tkinter as tk
from tkinter import font
# Configurar una fuente en negrita y cursiva
fuente_personalizada = font.Font(family="Segoe UI", size=18, weight="bold", slant="italic")

fuente_personalizada_costos = font.Font(family="Comic Sans", size=15, weight="bold", slant="italic")




#-------------------------------Configuramos los checkbuton de las listas de comida y bebidas-------------------------
#-------------------------------Configuramos los checkbutoon de la camida---------------------------------------------
for comida in lista_comidas:
    # Aqui crea los checkbuton
    variables_comida.append('')
    variables_comida[contador] =IntVar()# convertimos la variable string a integer
    comida = Checkbutton(panel_comida,
                         text=comida.title(),
                         font=(fuente_personalizada),
                         onvalue=1,
                         offvalue=0,
                         variable= variables_comida[contador],
                         command=revisar_check_comida)
    comida.grid(row=contador ,
                 column=0,
                   sticky=W )

    # Aqui crea los cuadros de entrada
    #----------------------Cuadro comida-----------------------------------------------------------------------------
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comida,
                                     font= (fuente_personalizada),
                                     bd=1,
                                     width= 6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador]) #boton desabilitado por defecto
    
    cuadros_comida[contador].grid(row=contador,
                                    column=1
                                    )
    contador +=  1

#-------------------------------Configuramos los checkbutoon de la bebida---------------------------------------------
variables_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] =IntVar()# convertimos la variable string a integer
    bebida = Checkbutton(panel_bebida,
                         text=bebida.title(),
                         font=(fuente_personalizada),
                         onvalue=1,
                         offvalue=0,
                         variable= variables_bebida[contador],
                         command=revisar_check_bebida)
    bebida.grid(row=contador , column=0, sticky=W )
#----------------------Cuadro bebida-----------------------------------------------------------------------------
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebida,
                                     font= ('Dosis', 18 , 'bold'),
                                     bd=1,
                                     width= 6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador]) #boton desabilitado por defecto
    
    cuadros_bebidas[contador].grid(row=contador,
                                    column=1)
    contador +=  1

#-------------------------------Configuramos los checkbutoon de los postres---------------------------------------------
variables_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] =IntVar()# convertimos la variable string a integer
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=(fuente_personalizada),
                         onvalue=1,
                         offvalue=0,
                         variable= variables_postre[contador],
                        command=revisar_check_postre)
    postre.grid(row=contador , column=0, sticky=W )

    #----------------------Cuadro postres-----------------------------------------------------------------------------
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font= ('Dosis', 18 , 'bold'),
                                     bd=1,
                                     width= 6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador]) #boton desabilitado por defecto
    
    cuadros_postres[contador].grid(row=contador,
                                    column=1
                                    )
    contador +=  1

#Etiquetas de costo y campos de entradas
# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo de comida',
                              font=(fuente_personalizada_costos),
                              bg='gray',
                              fg='white')
etiqueta_costo_comida.grid(row=0,column=0)  
# Entry es un widgets que permite el ingreso de texto
texto_costo_comida= Entry(panel_costos,
                          font=fuente_personalizada_costos,
                          bd=1,
                          state='readonly',
                          textvariable=var_costo_comida)
texto_costo_comida.grid(row=0 ,column=1)

#Etiquetas de costo y campos de entradas
# variables
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo de Bebidas',
                              font=(fuente_personalizada_costos),
                              bg='gray',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)  
# Entry es un widgets que permite el ingreso de texto
texto_costo_bebida= Entry(panel_costos,
                          font=fuente_personalizada_costos,
                          bd=1,
                          state='readonly',
                          textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1 ,column=1)

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo de Postres',
                              font=(fuente_personalizada_costos),
                              bg='gray',
                              fg='white')
etiqueta_costo_postre.grid(row=2,column=0)  
# Entry es un widgets que permite el ingreso de texto
texto_costo_postre= Entry(panel_costos,
                          font=fuente_personalizada_costos,
                          bd=1,
                          state='readonly',
                          textvariable=var_costo_postre)
texto_costo_postre.grid(row=2 ,column=1)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=(fuente_personalizada_costos),
                              bg='gray',
                              fg='white')
etiqueta_subtotal.grid(row=0,column=2)  
# Entry es un widgets que permite el ingreso de texto
texto_subtotal= Entry(panel_costos,
                          font=fuente_personalizada_costos,
                          bd=1,
                          state='readonly',
                          textvariable=var_subtotal)
texto_subtotal.grid(row=0 ,column=3)

etiqueta_impuesto = Label(panel_costos,
                              text='Impuestos 0.07%',
                              font=(fuente_personalizada_costos),
                              bg='gray',
                              fg='white')
etiqueta_impuesto.grid(row=1,column=2)  
# Entry es un widgets que permite el ingreso de texto
texto_impuesto= Entry(panel_costos,
                          font=fuente_personalizada_costos,
                          bd=1,
                          state='readonly',
                          textvariable=var_impuesto)
texto_impuesto.grid(row= 1,column=3)

etiqueta_total = Label(panel_costos,
                              text='Precio Final',
                              font=(fuente_personalizada_costos),
                              bg='gray',
                              fg='white')
etiqueta_total.grid(row=2,column=2)  
# Entry es un widgets que permite el ingreso de texto
texto_total= Entry(panel_costos,
                          font=fuente_personalizada_costos,
                          bd=1,
                          state='readonly',
                          textvariable=var_total)
texto_total.grid(row=2 ,column=3)

#------------------------------Agregamos los botones----------------------------------------------------------------------
#botones
botones = ['total','recibo','guardar','Recetear Todo',]
botones_creados = []
columnas= 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=(fuente_personalizada_costos),
                   fg='white',
                   bg='#B03060',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    
    boton.grid(row=0,
               column=columnas,
               padx=(5), # Espaciado horizontal (padding externo)
               pady=1 ,  # Espaciado vertical (padding externo)
               sticky="nsew")  # Expande el botón para ocupar más espacio dentro de su celda (opcional))
    columnas += 1    
botones_creados[0].config(command= calcular_total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=recetear_all)



#---------------------------Agregamos el area de recibo-----------------------------------------------------------------
texto_recibo = Text(panel_recibo,
                    font=(fuente_personalizada_costos),
                    width=45,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

#--------------------------Agregamos la calculadora--------------------------------------------------------------

visor_calculadora = Entry(panel_calculadora,
                          font=(fuente_personalizada_costos),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)
botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','*','=','Borrar','0','/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=(fuente_personalizada_costos),
                   fg='black',
                   bg='#90EE90',
                   bd=2,
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna,
               padx=(1,1), # Espaciado horizontal (padding externo)
               pady=5 ,  # Espaciado vertical (padding externo)
               sticky="nsew")
    if columna == 3:#si columna es igual a 3 quiere decir que estamos en la ultima columna, incrementamos una fila asi baja
        fila +=1
    columna += 1 
    if columna == 4:
        columna = 0 

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=click_borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))


# Evitar que la aplicacion se cierre
aplicacion.mainloop()