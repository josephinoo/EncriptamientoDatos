
import numpy as np 
from tkinter import *
import smtplib
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


def save():
    tamaño_de_matriz_info=tamaño_de_matriz.get()
    texto_incriptar_info=texto_incriptar.get()
    email_info=email.get()
    mcod=matrices_aleatorias_orden_n(tamaño_de_matriz_info)
    texto=texto_incriptar_info
    vector=vector_abc(diccionario,texto)
    vector=separador(vector,tamaño_de_matriz_info)
    resultado=str(producto_of_matrix_hecha_lista(mcod,vector))
    print(resultado)
    file = open("user.txt", "w")
    file.write(texto + "\n")
    file.write(resultado)
    file.close()
    """enviarcorreo"""
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
 
    # Iniciamos los parámetros del script
    remitente = 'josdavilalvarez@gmail.com'
    destinatarios = [email_info]
    asunto = '[RPI] Correo de prueba'
    cuerpo = 'Codigo Secreto de la Espol'
    ruta_adjunto = 'user.txt'
    nombre_adjunto = 'user.txt'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
 
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
 
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
 
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')
 
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
 
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
 
    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    sesion_smtp.login('josdavilalvarez@gmail.com','Espol1998')

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

        # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatarios, texto)

    # Cerramos la conexión
    sesion_smtp.quit()
    print(" Text has been registered successfully")
    tamaño_de_matriz_entry.delete(0, END)
    texto_incriptar_entry.delete(0, END)
   


    
    


screen=Tk()
screen.geometry("650x400+0+0")
screen.title("PROYECTO DE ALGEBRA LINEAL")
#IMAGEN
imagen=PhotoImage(file="algebra-lineal.gif")
imagenlogo=PhotoImage(file="descarga.gif")
lbl=Label(screen,image=imagen).place(x=0,y=0)
lblogo=Label(screen,image=imagenlogo).place(x=50,y=10)
"""X"""
tamaño_de_matriz_texto=Label(text="INGRESE EL TAMAÑO DE LA MATRIZ")
texto_incriptar_texto=Label(text="INGRESE EL TEXTO QUE DESEA ENCRIPTAR")
texto_email =Label(text="INGRESE EL EMAIL")
tamaño_de_matriz_texto.place(x=0,y=120)
texto_incriptar_texto.place(x=0,y=180)
texto_email.place(x=0,y=240)
tamaño_de_matriz=IntVar()
texto_incriptar=StringVar()
email=StringVar()


tamaño_de_matriz_entry=Entry(textvariable=tamaño_de_matriz,width="15")
texto_incriptar_entry=Entry(textvariable=texto_incriptar,width="30")
email_entry=Entry(textvariable=email,width="30")
tamaño_de_matriz_entry.place(x=250,y=120)
texto_incriptar_entry.place(x=300,y=180)
email_entry.place(x=150,y=240)

encriptar=Button(text="Encriptar",width="30",height="2",command=save)
encriptar.place(x=200,y=300)


mainloop()