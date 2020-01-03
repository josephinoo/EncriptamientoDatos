
import numpy as np 
diccionario = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,
"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
deccionariodescoficador={"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i","10":"j","11":"k","12":"l","13":"m",
"14":"n","15":"o","16":"p","17":"q","18":"r","19":"s","20":"t","21":"u","22":"v","24":"w","24":"x","25":"y","26":"z"}
"""tranforma el texto en lista removiendo los espacios en blanco"""
def texto_lista(texto):
    texto=texto.replace(' ', '')
    ltexto=list(texto.lower())
    return ltexto
"""el texto se agregran con el valor deficinido en el diccionario"""
def vector_abc(diccionario,texto):
    ltexto=texto_lista(texto)
    vector=[]
    for letra in ltexto:
        vector.append(diccionario[letra])
    return vector
"""Separa la lista  en la dimension de la matrix, y se agrega el valor de x al final si el division 
si no es exacta"""

def separador(vector,dimension):
    vector=vector
    datos=len(vector)
    if (datos%int(float(dimension)))==0:
        vectornuevo = []
        for i in range(0, len(vector), dimension):
            vectornuevo.append(vector[i:i+dimension])
        return vectornuevo
    else:
        valor= dimension-(datos%dimension)
        for agg in range(valor):
            vector.append(24)
        vectornuevo = []
        for i in range(0, len(vector), dimension):
            vectornuevo.append(vector[i:i+dimension])
        return vectornuevo
"""multiplicacion entre dos matrices"""
def producto_of_matrix_hecha_lista(matrizcodificadora,vector_a_codificiar):
    textoencriptado=[]
    vectores=[]
    for matrix_crip in vector_a_codificiar:
        matrix_codificada=np.dot(matrizcodificadora,np.array(matrix_crip))
        textoencriptado.append(matrix_codificada.tolist())
    for matrix  in textoencriptado:
        for vecot1 in matrix:
            vectores.append(vecot1)
    vectoresstri=" ".join( [str(i) for i in vectores])
    return vectoresstri

#Problema 1
Mcod = np.array ([[1 ,-1 ,0] ,[4 ,-2 ,3] ,[2 ,1 ,5]])
#Matriz inversa,funcion  que va descoficar
Mdecod = np.linalg.inv(Mcod)
texto="MOZART CONQUISTA A TODOS"

vector=vector_abc(diccionario,texto)
vector=separador(vector,3)
#print("Frase incriptada es:",producto_of_matrix_hecha_lista(Mcod,vector))
#Decifrar la los vectores
vector_ha_decifrar=[8,63,66,2,106,161,-2,1,10,-6,19,53,-6,96,180]
def sep_vectorcodificado(vectortexto,dimension):
    datos=len(vectortexto)
    if (datos%dimension)==0:
        vectornuevo = []
        for i in range(0, len(vectortexto), dimension):
            vectornuevo.append(vectortexto[i:i+dimension])
        return vectornuevo
def descoficador(vector,Mdecodifecadora,diccionario):
    textodescodificado=[]
    textodescodificado_ready=[]
    for matrix_crip in vector:
        matrix_decodificada=np.dot(Mdecodifecadora,np.array(matrix_crip))
        textodescodificado.append(matrix_decodificada.tolist())
    for lista in textodescodificado:
        for numero in lista:
            letra=str(int(numero))
            textodescodificado_ready.append(diccionario[letra])
    return " ".join(textodescodificado_ready)
descodi=sep_vectorcodificado(vector_ha_decifrar,3)
resultado_problema1=descoficador(descodi,Mdecod,deccionariodescoficador)

"""Problema 2"""
def matrices_aleatorias_orden_n(n):
    sigue="play"
    while sigue=="play":
        p=np.random.random_integers (1, 3, (n, n))
        det=np.linalg.det(p)
        if det==1 or det==-1:
            sigue="stop"
            return p
Mcod=matrices_aleatorias_orden_n(7)
texto="Euclides se encontraba impartiendo una clase en Alejandria cuando uno de sus alumnos le pregunto que para que servian todas aquellas demostraciones tan extensas y complejas que explicaba el matematico Pausadamente  Euclides se dirigio a otro de los estudiantes presentes y le dijo  Dale una moneda y que se marche Lo que este busca no es el saber esotracosa"
vector=vector_abc(diccionario,texto)
vector=separador(vector,7)
resultado=str(producto_of_matrix_hecha_lista(Mcod,vector))
"""INTERFAZ"""

from tkinter import*
from tkinter import messagebox

ventana=Tk()
ventana.geometry("650x400+0+0")
ventana.title("PROYECTO DE ALGEBRA LINEAL")
#IMAGEN
imagen=PhotoImage(file="algebra-lineal.gif")
imagenlogo=PhotoImage(file="descarga.gif")
lbl=Label(ventana,image=imagen).place(x=0,y=0)
lblogo=Label(ventana,image=imagenlogo).place(x=50,y=10)
#ventana.mainloop()
"""Inicio"""
def imprimir():
    vector=vector_abc(diccionario,str(valor3))
    vector=separador(vector,valor1)
    encriptado=str(producto_of_matrix_hecha_lista(matrices_aleatorias_orden_n(valor1),vector))
    return encriptado
frase_incriptar=StringVar()
valordado=StringVar()
"""Ingresar Valore"""
etiqueta_ingre=Label(ventana,text="Ingrese el tamaño de la Matriz",font=("Helvica",16))
etiqueta_ingre.place(x=50,y=150)
caja_ingre=Entry(ventana)
caja_ingre.grid(row = 1, column = 2)
caja_ingre.place(x=300,y=150)
valor1=caja_ingre.get()
print(valor1)
etiqueta_encrip=Label(ventana,text="Texto encriptar",font=("Helvica",16))
etiqueta_encrip.place(x=50,y=180)
caja_encrip=Entry(ventana,textvariable=frase_incriptar)
caja_encrip.place(x=300,y=180)
valor3=caja_encrip.get()

btn=Button(ventana,text="Encriptar",height=3 ,width=10,command=imprimir)
btn.place(x=300 ,y=210)
cuadro_incriptar=Listbox(ventana ,width=50,height=4)
cuadro_incriptar.place(x=120,y=300)
ventana.mainloop()



