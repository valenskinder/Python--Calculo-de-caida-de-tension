#Programa para calcular las caidas de tension en los cables eléctricos.

from tkinter import *

raiz=Tk() #Creacion raiz

raiz.title("Caida de tension en cables eléctricos.")

miFrame=Frame(raiz) #Creacion frame

miFrame.pack() #Empaquetamiento frame
#****************************************************************Titulo*********************************************************************

titulo=Label(miFrame,text="Cálculo de caida de tensión",justify="right")
titulo.grid(row=0,column=0)
titulo.config(fg="black")
titulo.config(font=("verdana",20))

#**********************************************************Creacion RadioButtom*************************************************************
s=0

def TipoCaida(): #Funcion para seleccionar si calculamos caida de tension normal o en arranque.

    global s

    if variable_boton_eleccion.get()==1:

        label_corriente_nom.config(text="Corriente nominal [Amper]: ")
        avisoPorcen.config(text="El 5 % correspondiente a la tension nominal es: ")
        deltaU.config(text="ΔU [Volt]: ")
        s=1
    
    else:

        label_corriente_nom.config(text="Corriente durante el arranque [Amper]: ")
        avisoPorcen.config(text="El 15 % correspondiente a la tension nominal es: ")
        deltaU.config(text="ΔU en el arranque [Volt]: ")
        s=2

const=0

def TipoCirc():

    global const

    if variable_boton.get()==1:

        const=2
    
    else:

        const=1.73

variable_boton_eleccion=IntVar() #Declaro una variable tipo INT
variable_boton=IntVar() 

botonElecUno=Radiobutton (miFrame,text="Caida de tension.", variable=variable_boton_eleccion,value=1,command=TipoCaida)
botonElecUno.grid(row=1, column=0)

botonElecDos=Radiobutton (miFrame,text="Caida de tension en arranque", variable=variable_boton_eleccion,value=2,command=TipoCaida)
botonElecDos.grid(row=1, column=1)


boton=Radiobutton (miFrame,text="Circuito monofásico.", variable=variable_boton,value=1,command=TipoCirc)
boton.grid(row=2, column=0)

botonDos=Radiobutton (miFrame,text="Circuito trifásico.", variable=variable_boton,value=2,command=TipoCirc)
botonDos.grid(row=2, column=1)


#**********************************************************Creacion de label y cuadros de texto*********************************************
label_tension_nom=Label(miFrame, text="Tensión nominal [Volt]: ")
label_tension_nom.grid (row=6 , column=0)

valorTensionNominal=StringVar() #Cuadro de texto para tension nominal
TensionNominal=Entry (miFrame,justify="right",textvariable=valorTensionNominal)
TensionNominal.grid (row=6, column=1, padx=10, pady=10)

label_corriente_nom=Label(miFrame)
label_corriente_nom.grid (row=7, column=0)

CorrienteNominal=Entry (miFrame,justify="right")
CorrienteNominal.grid (row=7, column=1,padx=10, pady=10)

label_longitud=Label(miFrame, text="Longitud [km]: ")
label_longitud.grid (row=8 , column=0)

longitud=Entry (miFrame,justify="right")
longitud.grid (row=8, column=1, padx=10, pady=10)

label_resistencia=Label(miFrame, text="Resistencia [Ω/Km]: ")
label_resistencia.grid (row=9 , column=0)

resistencia=Entry (miFrame,justify="right")
resistencia.grid (row=9, column=1, padx=10, pady=10)

label_reactancia=Label(miFrame, text="Reactancia [Ω/Km]: ")
label_reactancia.grid (row=10 , column=0)

reactancia=Entry (miFrame,justify="right")
reactancia.grid (row=10, column=1, padx=10, pady=10)

#****************************************************Creacion de los avisos de caida de tension admisible*****************************

avisoPorcen=Label(miFrame)
avisoPorcen.grid (row=20 , column=0)

cuadroAvisoPorc=Entry(miFrame, text="",background="black", fg="#03f943", justify="right")
cuadroAvisoPorc.grid (row=20 , column=1)

deltaU=Label(miFrame)
deltaU.grid (row=21 , column=0)

cuadroDeltaU=Entry(miFrame,background="black", fg="#03f943", justify="right")
cuadroDeltaU.grid (row=21 , column=1)

verificaDeltaU=Label(miFrame) #Label para indicar que verifica Delta U
verificaDeltaU.grid (row=21 , column=2)

warning=Label(miFrame) #Creo un label para realizar una advertencia
warning.grid (row=23,column=1)
#**********************************************************Función calcular****************************************************************
def Calcular(): #Declaro funcion Calcular.

    #Procedimiento para verificar si ingreso solo numeros en los cuadros de texto.En el caso que ingrese una letra, me lo indicara una advertencia.
    #Con replace, cambio el "." por un "1" para poder evaluar si es un digito lo que ingreso en el cuadro de texto.

    uno=TensionNominal.get().replace(".","1").isdigit()
    dos=CorrienteNominal.get().replace(".","1").isdigit()
    tres=longitud.get().replace(".","1").isdigit()
    cuatro=resistencia.get().replace(".","1").isdigit()
    cinco=reactancia.get().replace(".","1").isdigit()

        
    if uno and dos and tres and cuatro and cinco==True: #Evaluacion del ingreso de datos.

        warning.config(text="Los datos fueron ingresados correctamente.")

    #Comienzo de los calculos.
        global const
        global s

        valorTenNom=TensionNominal.get() #Obtengo lo que escribi en el cuadro correspondiente a tension nominal.
        cincoPorc=float(valorTenNom)*(0.05) #realizo la operacion para obtener el 5 %.
        quincePorc=float(valorTenNom)*(0.15) #realizo la operacion para obtener el 15 %.
    
    
        resis=float(resistencia.get()) #Guardo en una variable el valor de resistencia colocado en el cuadro de texto.
        reac=float (reactancia.get()) #Guardo en una variable el valor de reactancia colocado en el cuadro de texto.
        i=float(CorrienteNominal.get()) #Guardo en una variable el valor de corriente nominal colocado en el cuadro de texto.
        longit=float (longitud.get()) #Guardo en una variable el valor de longitud colocado en el cuadro de texto.

        if s==1:

            calcDeltaU=(const)*(i)*(longit)*((resis*0.85)+(reac*0.53)) #Calculo de la caida de tension normal.
            cuadroDeltaU.insert(0,round(calcDeltaU,4)) #Inserto el resultado de la caida de tension normal en el cuadro de texto correspondiente.
    #Con round en el primer parametro llamo a calcDeltu y en el segundo, indico cuantos numeros coloco en pantalla.
            cuadroAvisoPorc.insert(0,cincoPorc)
        #**********************************Evaluacion para saber si verifica el conductor**********************************************

            if calcDeltaU < cincoPorc: #Evaluacion para saber si verifica en funcionamiento normal.

                verificaDeltaU.config(text="La caida de tension es menor a lo permitido. VERIFICA ", bg="green")

            else:

                verificaDeltaU.config(text="La caida de tension es mayor a lo permitido. NO VERIFICA ", bg="red")
    
        else:

            calcDeltaU=(const)*(i)*(longit)*((resis*0.35)+(reac*0.94)) #Calculo de la caida de tension en el arranque.
            cuadroDeltaU.insert(0,round(calcDeltaU,4)) 
            cuadroAvisoPorc.insert(0,quincePorc)

            if calcDeltaU < quincePorc: #Evaluacion para saber si verifica en funcionamiento normal.

                verificaDeltaU.config(text="La caida de tension es menor a lo permitido en el arranque. VERIFICA ", bg="green")

            else:

                verificaDeltaU.config(text="La caida de tension es mayor a lo permitido en el arranque. NO VERIFICA ", bg="red")

    else:

        warning.config(text="Algunos de los datos se ingresaron incorrectamente.VERIFIQUE",bg="red")

def Borrar (): #Funcion borrar. Borro todo lo ingresado en los cuadros de texto de parámetros y resultados.

    TensionNominal.delete(0,END)
    CorrienteNominal.delete(0,END)
    longitud.delete(0,END)
    resistencia.delete(0,END)
    reactancia.delete(0,END)
    cuadroAvisoPorc.delete(0,END)
    cuadroDeltaU.delete(0,END)
    verificaDeltaU.config(text="")
    warning.config(text="")
    
#****************************************************Creacion del boton calcular******************************************************

botonCalcular=Button(miFrame,text="CALCULAR",command=lambda:Calcular())
botonCalcular.config(width=35,height=2)
botonCalcular.grid(row=15, column=0, padx=10, pady=10,columnspan=4,rowspan=3)

#****************************************************Creacion del boton borrar******************************************************
botonBorrar=Button(miFrame,text="BORRAR TODO",command=lambda:Borrar())
botonBorrar.config(width=35,height=2)
botonBorrar.grid(row=15, column=1, padx=10, pady=10,columnspan=4,rowspan=3)

raiz.mainloop()