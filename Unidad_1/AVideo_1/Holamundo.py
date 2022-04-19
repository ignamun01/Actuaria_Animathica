#col = ["rojo","verde","azul"]
#for i in col :
 #   print(i)

#cad = "Hola mundo"
#for i in cad :
#    print(i)



#for i in range(8) :
#  print(i)

#for i in range(3,8) :
 #     print(i)

#suma, numero = 0, 1
#while numero <= 10:
  #  suma = numero + suma
   # numero = numero + 1
#print("La suma es " + str(suma))

#val = 1
#fin = 10
#while(val < fin):
#    print(val)
#    val = val + 1

#va = 1
#fin = 10 
#while (va < fin):
 # print(va)
#  va= va + 1

#va = 1
#fin = 10 
#while (va < fin):
 # print(va)
#  va= va + 1
 # if (va == 5):
#  break

#val = 1
#fin = 10
#while(val < fin):
#    val = val + 1
#    if(val == 6):
#        continue
#    print(val)

#diccionario = {"manzana":"apple" , "naranja":"orange" , "platano":"banana" , "limon":"lemon" }
#print(diccionario["naranja"])
#diccionario["piña"] = "pinapple"
#print(diccionario)
#for i,j in diccionario.items():
#    print("{} en inglés es {}".format(i,j))

#nota = 4.5
#tr = "si"
#if(nota >= 4) and tr == "si" :
#  print("aprovado")
#else:
#    print("suspenso")

#class claseSilla :
#  color = "blanco"
#  precio = 100
#objetoSilla1 = claseSilla()
#print(objetoSilla1.color)
#print(objetoSilla1.precio)
#objetoSilla2 = claseSilla
#objetoSilla2.color = "verde"
#objetoSilla2.precio = 120
#print(objetoSilla2.color)
#print(objetoSilla2.precio)

#class Persona :
#  def __init__(self,nombre,edad):
#     self.nombre = nombre
#     self.edad = edad
#  def saludar(self):
#    print("Hola,me llamo {} y tengo {} años".format(self.nombre,self.edad))

#persona1 = Persona("juan",35)
#print(persona1.edad)
#print(persona1.nombre)
#print(persona1.saludar())

#def saludar ():
#  print("Buenos días")
#
#print(saludar())
#
#def saludar(nombre):
#  print("Buenos días " + nombre)
#
#nombre = "Antonio"
#
#print(saludar(nombre)) 

#def suma(num1,num2):
#  suma = num1 + num2
#  return suma
#
#n1 = 5
#n2 = 3
#resultado = suma(n1,n2)
#print(resultado) 
#
#colores =["rojo","verde", "azul"]

#def incluir_color(colores,color):
# colores.append(color)
#
#color = "negro"
#incluir_color(colores,color)
#
#print(colores)


#resultado = lambda numero : numero + 30
#print(resultado( 10 ) )


#resultado2 = lambda num1,num2 :num1 + num2
#print(resultado2(5,6))


#class Coche:
# def __init__(self, marca, color, combustible, cilindrada ):
#    self.marca = marca
#    self.color = color
#    self.combustible = combustible
#    self.cilindrada = cilindrada
# def mostrar_caracteristicas(self):
#   print("La marca es {},es de color {},usa combustible{} y tiene una cilindrada de {}".format(self.marca, self.color, self.combustible, self.cilindrada))
#coche1 = Coche("opel","rojo","gasolina","1.6")
#print(coche1.mostrar_caracteristicas())



#media = lambda num1,num2,num3 : (num1+num2+num3)/3
#print(media(3,3,3))

#try:
#  num1 = 8
#  num2 = 0
#  division = num1/num2
#  print(division)
#except:
#  print("Ha habido un error")

#try:
#  num1 = 8
#  num2 = 0
#  division = num1/num2
#  print(division)
#except ZeroDivisionError:
#  print("Error,division entre cero")

#try:
#  num1 = 8
#  num2 = 7
#  division = num1/num2
#  print(division)
#except ZeroDivisionError:
#  print("Error,division entre cero")
#except:
#  print("Ha habido un error")
#else:
#  print("La division funciono correctamente")


#try:
#  num1 = 8
#  num2 = 0
#  division = num1/num2
#  print(division)
#except ZeroDivisionError:
#  print("Error,division entre cero")
#except:
#  print("Ha habido un error")
#else:
#  print("La division funciono correctamente")
#finally:
#  print("Esta prueba del try se ha acabado")

#try:
# num1 = 6
# num2 = 3
# num3 = 3
# resta = num2 - num3
# operacion = num1 / resta
# print(operacion)
#except:
#  print("Hay un error")



#def operacion(num1,num2,num3):
#  resultado = num1 /(num2-num3)
#  return(resultado)
#num1 = 6
#num2 = 3
#num3 = 3
#try:
# resultado = operacion(num1,num2,num3)
# print(resultado)
#except:
#  print("DIvision entre cero")


########expresiones regulares
#texto = "Hola,mi nombre es antonio"
#import re
#resultado = re.search("nombre",texto)
#if(resultado):
#  print("cadena encontrada")
#else:
#  print("cadena no encontrada")

#import re
#texto = """ 
#El coche de luis es rojo,
#el coche de antonio es blanco,
#el coche de maria es rojo
#"""
#resultado = re.findall("coche.*rojo",texto)
#print(resultado)

#import re
#texto = "La silla es blanca y vale 80"
#resultado = re.split("\s",texto)
#print(resultado)


#import re
#texto = "La silla es blanca y vale 80"
#resultado = re.sub("blanca","roja",texto)
#print(resultado)

#import json
#producto1 = {"nombre":"silla","color":"blanco","precio":80}
#estructura_json = json.dumps(producto1)
#print(estructura_json)


#from datetime import datetime
#fechayhora = datetime.now()
#print(fechayhora)
#
#año = fechayhora.year
#mes = fechayhora.month
#dia = fechayhora.day
#
#hora = fechayhora.hour
#minuto = fechayhora.minute
#segundo = fechayhora.second
#
#print("La hora es {}:{}:{}".format(hora,minuto,segundo))


#import re
#def buscar(palabra,texto):
#  resultado = re.search(palabra,texto)
#  return resultado
#
#texto = "Esta es una frase de prueba para hacer busqeudas"
#palabra = "frase"
#
#resultado = buscar(palabra,texto)
#if(resultado):
#  print ("palabra {} encontrada".format(palabra))
#  inicia = resultado.start()
#  final = resultado.end()
#  print("Empieza en la posicion {} y finaliza en la posicion {}".format(inicia,final))
#else:
#  print("palabra {} no encontrada".format(palabra))


#import sqlite3
#
#conexion = sqlite3.connect("basededatos1.db")
#
#conexion.close()

#import tkinter
#
#raiz = tkinter.Tk()
#raiz.title("Mi programa")
#
#raiz.mainloop()


#import tkinter
#raiz = tkinter.Tk()
#raiz.title("Mi programa")
      #creamos el componente frame
#frame = tkinter.Frame(raiz)
#frame.config(bg = "blue",width = 400,height = 300)
#frame.pack()
#
#raiz.mainloop()


#import tkinter
#raiz = tkinter.Tk()
#raiz.title("Mi programa")

    #creamos el componente label(etiqueta)
#texto = "Hola mundo"
#etiqueta = tkinter.Label(raiz,text = texto)
#etiqueta.config(fg = "green",bg = "lightgrey",font = ("Cortana",30))
#etiqueta.pack()
#raiz.mainloop()


#import tkinter
#raiz = tkinter.Tk()
#raiz.title("Mi programa")
    #creamos el componente entry(entrada de datos)
#entrada = tkinter.Entry(raiz)
#entrada.config(justify = "center",show ="*")
#entrada.pack()
#
#raiz.mainloop()


#import tkinter
#raiz = tkinter.Tk()
#raiz.title("Mi programa")
    #creamos el componente text(texto largo)
#entrada = tkinter.Text(raiz)
#entrada.config(width = 20,height = 10,font =("Verdana",15),padx = 10,pady = 10 ,fg = "green",selectbackground = "lightgrey")
#entrada.pack()
#
#raiz.mainloop()


#import tkinter
#raiz = tkinter.Tk()
#raiz.title("Mi programa")
    #creamos el componente buttom
    #definimos la funcion accion
#def accion():
#  print("Hola mundo")

#boton = tkinter.Button(raiz,text="Ejecutar",command = accion)
#boton.config(fg = "green")
#boton.pack()
#
#raiz.mainloop()



#import tkinter
#raiz = tkinter.Tk()
#raiz.title("Mi programa")

    #crear los radiobutton
    #creamos la funcion seleccionar
#def seleccionar():
#  print("La opcion seleccionada es {}".format(opcion.get()))

#opcion = tkinter.IntVar()
#radiobutton1 = tkinter.Radiobutton(raiz,text = "Opcion1",variable = opcion,value= 1,command = seleccionar)
#radiobutton1.pack()
#
#radiobutton2 = tkinter.Radiobutton(raiz,text = "Opcion2",variable = opcion,value= 2,command = seleccionar)
#radiobutton2.pack()
#
#radiobutton3 = tkinter.Radiobutton(raiz,text = "Opcion3",variable = opcion,value= 3,command = seleccionar)
#radiobutton3.pack()
#
#raiz.mainloop()


#import tkinter
#raiz = tkinter.Tk()
#raiz.title("Mi programa")

    #crear nuestro checkbutton
#def verificar():
#  valor = check1.get()
#  if(valor == 1):
#    print("El check esta activado")
#  else:
#    print("El check esta desactivado")
#
#check1 = tkinter.IntVar()
#
#boton1 = tkinter.Checkbutton(raiz,text="Opcion1",variable = check1,onvalue = 1,offvalue = 0,command = verificar)
#boton1.pack()
#
#raiz.mainloop()



#import tkinter
#from tkinter import messagebox
#raiz = tkinter.Tk()
#raiz.title("Mi programa")

    #crear "popup"(ventana de informacion)
#def avisar():
#  tkinter.messagebox.showinfo("Titulo","Mensaje con la informacion")
#
#boton = tkinter.Button(raiz,text = "Pulsar para aviso",command = avisar)
#boton.pack()
#
#raiz.mainloop()


#import tkinter
#from tkinter import messagebox
#
#raiz = tkinter.Tk()
#raiz.title("Mi programa")

    #crear "popup"(ventana de pregunta o confirmar)
#def preguntar():
#  resultado = tkinter.messagebox.askquestion("Titulo de la pregunta","¿Quieres borrar este fichero?")
#  if(resultado =="yes"):
#    print("Si,quiero borrarlo")
#  else:
#    print("No,no quiero borrarlo")
#
#boton = tkinter.Button(raiz,text = "Pulsar para preguntar",command = preguntar)
#boton.pack()
#
#raiz.mainloop()


#import tkinter
#from tkinter import filedialog
#
#raiz = tkinter.Tk()
#raiz.title("Mi programa")

    #crear "popup"(ventana de pregunta o confirmar)
#def abrirfichero():
#  rutafichero = filedialog.askopenfilename(title = "Abrir un fichero")
#  print(rutafichero)
#boton = tkinter.Button(raiz,text = "Pulsar para empezar",command = abrirfichero)
#boton.pack()
#raiz.mainloop()


#def saludar(nombre):
#    """
#    Esto sera un comentario de la funcion saludar
#    Esta funcion recibira como parametro una cadena con el nombre e
#    omprimira por pantalla un saludo con el nombre concatenado
#    """
#    print("Bueno dias " + nombre)
# 
#saludar("Antonio")
#
#help(saludar)

#class Saludos:
#    """
#    Esta clase tendra dos funciones BUenos dias y adios
#    """
#
#    def buenosdias(self,nombre):    #con self,no estamos refiriendo a la clase
#        """
#        Esta funcion sirve para decir buenos dias
#        """
#        print("Buenos dias {}".format(nombre))
#
#    def adios(self,nombre):
#        """
#        Esta funcion dice aduis a una persona
#        """
#        print("Adios {}".format(nombre))
#
#saludo = Saludos()
#saludo.buenosdias("Luis")
#saludo.adios("Luis")
#
#help(Saludos)




#for numero in range(11):
#    print(numero)



#def pares(maximo):
#    for i in range(maximo):
#        if(i % 2 == 0):
#            yield i
#
#maximo = 11
#for i in pares(maximo):
#    print(i)


#def positivo(num):
#    if(num > 0):
#        return True
#    else :
#        return False
#       
#numeros= [4,-2,8,-3,-5,-7,1,9]
#filtro = filter(positivo,numeros)
#resultado = list(filtro)
#print(resultado)



#def mult(num):
#    return num * 2
#
#numeros = [2,4,6]
#
#mapeo = map(mult,numeros)
#resultado = list(mapeo)
#print(resultado)
#
#lista_resultados = list(map(mult,numeros))
#print(lista_resultados)
#
#lista_resultados2 = list(map(lambda  nume : nume * 2,numeros))
#print(lista_resultados2)


numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

#
#def primos(maximo):
#    for i in range(maximo):
#        if(i in numeros_primos):
#            yield i
#        if (i > 100):
#            break
#
#maximo = 50
#for i in primos(maximo):
#    print(i)
     
       



























